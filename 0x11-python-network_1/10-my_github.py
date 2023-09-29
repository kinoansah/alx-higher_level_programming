#!/usr/bin/python3
# A script that takes GitHub credentials and uses the GitHub API to display your id
import requests
import sys

def get_github_id(username, password):
    # Define the GitHub API URL to fetch user details
    api_url = f'https://api.github.com/user'

    # Set up the Basic Authentication header with your username and personal access token
    auth = (username, password)

    # Send a GET request to the GitHub API
    response = requests.get(api_url, auth=auth)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response to get your GitHub ID
        user_data = response.json()
        return user_data.get('id')
    else:
        # If authentication fails, return None
        return None

if __name__ == "__main__":
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python 10-my_github.py <username> <personal_access_token>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]

    github_id = get_github_id(username, password)

    # Display the GitHub ID or None if authentication fails
    print(github_id)
