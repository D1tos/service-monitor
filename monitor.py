import os
import time
import logging
import smtplib

import click
import requests

from dotenv import load_dotenv
from email.message import EmailMessage

VERSION = "1.0.0"

load_dotenv()

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    handlers=[
        logging.FileHandler('logs/monitor.log'),
        logging.StreamHandler()
    ]
)

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

telegram_enabled = bool(TOKEN and CHAT_ID)

email_enabled = bool(
    EMAIL_SENDER and
    EMAIL_PASSWORD and
    EMAIL_RECEIVER
)

def send_telegram_message(message):
    if not telegram_enabled:
        return
    telegram_api_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    try:
        response = requests.post(telegram_api_url, data=data, timeout=5)

        if response.status_code != 200:
            logging.error("Failed to send Telegram message")

    except Exception as e:
        logging.error(f"Telegram ERROR: {e}")

def send_email(subject, body):
    if not email_enabled:
        logging.warning("Email alerts disabled")
        return

    message = EmailMessage()

    message["Subject"] = subject
    message["From"] = EMAIL_SENDER
    message["To"] = EMAIL_RECEIVER

    message.set_content(body)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()

            server.login(
                EMAIL_SENDER,
                EMAIL_PASSWORD
            )
            server.send_message(message)

        logging.info("Email alert sent")

    except Exception as e:
        logging.error(f"Email ERROR: {e}")

def check_website(url, timeout, retries=3):
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=timeout)

            if response.status_code == 200:
                return "UP"

            logging.warning(
                f"{url} returned status code {response.status_code}"
            )

        except Exception as e:
            logging.error(
                f"Attempt {attempt + 1}/{retries} failed for {url}: {e}"
            )

            if attempt < retries - 1:
                logging.warning(
                    f"Retrying {url} ({attempt + 1}/{retries})"
                )

                time.sleep(2)

    return "DOWN"

def send_alert(message, no_telegram):
    if not no_telegram:
        send_telegram_message(message)

    send_email(
        subject="Service Monitor Alert",
        body=message
    )

def build_status_message(current_url, current_status):
    if current_status == "DOWN":
        return f"🚨 {current_url} is DOWN"

    return f"✅ {current_url} is BACK UP"

def log_status_change(current_url, current_status):
    logging.info(
        f"STATUS CHANGE: {current_url} -> {current_status}"
    )

@click.command(
    help="CLI service monitoring tool with Telegram and Email alerts"
)
@click.option('--url', multiple=True, required=True, help='URL to monitor')
@click.option('--interval', default=10, type=click.IntRange(1, 3600), show_default=True, help='Check interval in seconds')
@click.option('--no-telegram', is_flag=True, help='Disable telegram alerts')
@click.option('--timeout', default=5, type=click.IntRange(1, 60), show_default=True, help='Request timeout in seconds')

def main(url, interval, no_telegram, timeout):
    last_status = {}

    logging.info(f"Service Monitor v{VERSION} started")

    for current_url in url:
        logging.info(f"Monitoring: {current_url}")

    logging.info(f"Check interval: {interval}s")
    logging.info(f"Request timeout: {timeout}s")

    try:
        while True:
            for current_url in url:
                current_status = check_website(
                    current_url,
                    timeout
                )

                if current_url not in last_status or last_status[current_url] != current_status:

                    message = build_status_message(
                        current_url,
                        current_status
                    )

                    send_alert(message, no_telegram)

                    log_status_change(
                        current_url,
                        current_status
                    )

                    last_status[current_url] = current_status
                else:
                    logging.info(
                        f"STATUS: {current_url} -> {current_status}"
                    )

            time.sleep(interval)

    except KeyboardInterrupt:
        logging.info("Service monitor stopped")

if __name__ == "__main__":
    main()