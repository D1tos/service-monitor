import requests

url = "https://google.com"

try:
    response = requests.get(url)

    if response.status_code == 200:
        print(f"{url} is UP")
    else:
        print(f"{url} is DOWN. Status Code: {response.status_code}")

except Exception as e:
    print("CRITICAL ERROR", e)
