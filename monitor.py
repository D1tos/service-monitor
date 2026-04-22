import requests
import datetime
import time

TOKEN = "8767610691:AAEMhGRyTnnJjNlH5XR9okAthuGI7oWiZko"
CHAT_ID = "350857578"

url = "https://google.com"

def send_telegram_message(message):
    telegram_api_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(telegram_api_url, data=data)

while True:
    try:
        response = requests.get(url,timeout=5)

        if response.status_code == 200:
            print(f"{datetime.datetime.now()} | {url} is UP")
        else:
            print(f"🚨 {url} is DOWN. Status Code: {response.status_code}")
            send_telegram_message(f"🚨 {url} is DOWN. Status Code: {response.status_code}")

    except Exception as e:
        print("CRITICAL ERROR", e)
        send_telegram_message(f"🔥 CRITICAL ERROR: {e}")

    time.sleep(10)