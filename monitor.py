import time
import click

from dotenv import load_dotenv

load_dotenv()

from utils.logger import logging
from monitoring.checker import check_website
from notifications.alerts import send_alert

VERSION = "1.0.0"

load_dotenv()

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