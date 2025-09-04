# Assisted by watsonx Code Assistant
import requests
import time

url = "https://www.google.com"
interval = 1  # seconds
duration = 60  # seconds

def get_http_status(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

status_codes = []
start_time = time.time()

while time.time() - start_time < duration:
    status = get_http_status(url)
    if status is not None:
        status_codes.append(status)
    time.sleep(interval)

print("Collected status codes:", status_codes)
