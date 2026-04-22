import requests

url = "https://google.com"

try:
    response = requests.get(url)
    print(response.status_code)
expect Exception as e:
    print("Ошибка", e)