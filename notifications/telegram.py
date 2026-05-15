import os
import requests
import logging

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