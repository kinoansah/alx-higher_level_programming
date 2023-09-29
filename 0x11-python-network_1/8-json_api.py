#!/usr/bin/python3
# A Python script that takes in a letter and sends a POST request
import requests
import sys

if len(sys.argv) == 1:
    q = ""
else:
    q = sys.argv[1]

url = "http://0.0.0.0:5000/search_user"

# Create a dictionary with the letter as a parameter
data = {'q': q}

try:
    response = requests.post(url, data=data)
    response.raise_for_status()  # Raise an exception for HTTP errors

    try:
        user_data = response.json()

        if user_data:
            user_id = user_data.get('id')
            user_name = user_data.get('name')
            print(f"[{user_id}] {user_name}")
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {str(e)}")
