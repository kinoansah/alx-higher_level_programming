#!/usr/bin/python3
# A Python script that fetches https://alx-intranet.hbtn.io/status
import requests

url = "https://alx-intranet.hbtn.io/status"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {str(e)}")
