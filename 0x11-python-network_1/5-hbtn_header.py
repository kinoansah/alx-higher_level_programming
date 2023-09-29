#!/usr/bin/python3
# A Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: ./5-hbtn_header.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Check if the 'X-Request-Id' header is present in the response
    if 'X-Request-Id' in response.headers:
        x_request_id = response.headers['X-Request-Id']
        print(x_request_id)
    else:
        print("X-Request-Id header not found in the response.")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {str(e)}")
