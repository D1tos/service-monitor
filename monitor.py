from dotenv import load_dotenv

import os
import requests
import datetime
import time

load_dotenv()

TOKEN = os."TOKEN"
CHAT_ID = os."CHAT_ID"

url = "https://google.com"

def send_telegram_message(message):
    telegram_api_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(telegram_api_url, data=data, timeout=5)

last_status = None

while True:
    try:
        response = requests.get(url,timeout=5)

        if response.status_code == 200:
            current_status = "UP"
        else:
            current_status = "DOWN"
    except Exception as e:
        print("ERROR:", e)
        current_status = "DOWN"

    if current_status != last_status:

        if current_status == "DOWN":
            send_telegram_message(f"🚨 {url} is DOWN")
        else:
            send_telegram_message(f"✅ {url} is BACK UP")

        print(f"{datetime.datetime.now()} | STATUS CHANGE: {current_status}")
        last_status = current_status
    else:
        print(f"{datetime.datetime.now()} | {url} is {current_status}")

    time.sleep(10)
