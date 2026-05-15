import requests
import logging
import time

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
                logging.warning(
                    f"Retrying {url} ({attempt + 1}/{retries})"
                )

                time.sleep(2)

    return "DOWN"