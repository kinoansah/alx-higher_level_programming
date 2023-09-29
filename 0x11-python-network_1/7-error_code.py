#!/usr/bin/python3
# A Python script that takes in a URL
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: ./7-error_code.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Check if the HTTP status code is greater than or equal to 400
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        # Print the response body
        print(response.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {str(e)}")
