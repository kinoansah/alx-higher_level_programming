#!/usr/bin/python3
# A Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.
import requests
import sys

if len(sys.argv) != 3:
    print("Usage: ./6-post_email.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

# Create a dictionary with the email as a parameter
data = {'email': email}

try:
    response = requests.post(url, data=data)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Print the response body
    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {str(e)}")
