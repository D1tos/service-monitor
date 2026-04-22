import requests
import datetime
import time

url = "https://google.com"

while True:
    try:
        response = requests.get(url)

        if response.status_code == 200:
            print(f"{datetime.datetime.now()} | {url} is UP")
        else:
            print(f"{url} is DOWN. Status Code: {response.status_code}")

    except Exception as e:
        print("CRITICAL ERROR", e)

    time.sleep(60)