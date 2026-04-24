from dotenv import load_dotenv

import os
import requests
import datetime
import time

load_dotenv()

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
URL = os.getenv("URL")

telegram_enabled = bool(TOKEN and CHAT_ID)

if not TOKEN or not CHAT_ID or not URL:
    raise ValueError("TOKEN, CHAT_ID or URL not set")

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

last_status = None


while True:
    try:
        response = requests.get(URL,timeout=5)

        if response.status_code == 200:
            current_status = "UP"
        else:
            current_status = "DOWN"
    except Exception as e:
        print("ERROR:", e)
        current_status = "DOWN"

    if current_status != last_status:

        if current_status == "DOWN":
            send_telegram_message(f"🚨 {URL} is DOWN")
        else:
            send_telegram_message(f"✅ {URL} is BACK UP")

        print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | STATUS CHANGE: {current_status}")
        last_status = current_status
    else:
        print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | STATUS: {current_status}")

    time.sleep(10)
