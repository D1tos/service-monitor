from dotenv import load_dotenv

import os
import requests
import datetime
import time
import click

load_dotenv()

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
            print("Failed to send Telegram message")

    except Exception as e:
        print("Telegram ERROR:", e)

@click.command()
@click.option('--url', multiple=True, required=True, help='URL to monitor')
@click.option('--interval', default=10, help='Check interval')
@click.option('--no-telegram', is_flag=True, help='Disable telegram alerts')

def main(url, interval, no_telegram):
    last_status = {}

    while True:
        for current_url in url:
            try:
                response = requests.get(current_url, timeout=5)

                if response.status_code == 200:
                    current_status = "UP"
                else:
                    current_status = "DOWN"
            except Exception as e:
                print("ERROR:", e)
                current_status = "DOWN"

            if current_url not in last_status or last_status[current_url] != current_status:

                if current_status == "DOWN":
                    message=f"🚨 {current_url} is DOWN"
                else:
                    message=f"✅ {current_url} is BACK UP"

                if not no_telegram:
                    send_telegram_message(message)

                print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | STATUS CHANGE: {current_url} -> {current_status}")
                last_status[current_url] = current_status
            else:
                print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | STATUS: {current_url} -> {current_status}")

        time.sleep(interval)

if __name__ == "__main__":
    main()