#!/usr/bin/python3
# A python script that takes in a URL
import urllib.request
import sys

if len(sys.argv) != 2:
    print("Usage: ./1-hbtn_header.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        # Check if the 'X-Request-Id' header is present in the response
        if 'X-Request-Id' in response.headers:
            x_request_id = response.headers['X-Request-Id']
            print(x_request_id)
        else:
            print("X-Request-Id header not found in the response.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
