from dotenv import load_dotenv

import os
import requests
import time
import click
import logging

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

telegram_enabled = bool(TOKEN and CHAT_ID)

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
                time.sleep(2)

    return "DOWN"

@click.command()
@click.option('--url', multiple=True, required=True, help='URL to monitor')
@click.option('--interval', default=10, help='Check interval')
@click.option('--no-telegram', is_flag=True, help='Disable telegram alerts')
@click.option('--timeout', default=5, help='Request timeout')

def main(url, interval, no_telegram, timeout):
    last_status = {}

    while True:
        for current_url in url:
            current_status = check_website(
                current_url,
                timeout
            )

            if current_url not in last_status or last_status[current_url] != current_status:

                if current_status == "DOWN":
                    message=f"🚨 {current_url} is DOWN"
                else:
                    message=f"✅ {current_url} is BACK UP"

                if not no_telegram:
                    send_telegram_message(message)

                logging.info(
                    f"STATUS CHANGE: {current_url} -> {current_status}"
                )
                last_status[current_url] = current_status
            else:
                logging.info(
                    f"STATUS: {current_url} -> {current_status}"
                )

        time.sleep(interval)

if __name__ == "__main__":
    main()