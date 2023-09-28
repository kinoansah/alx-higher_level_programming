#!/bin/bash

# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Get the URL from the command line argument
url="$1"

# Use curl to send a request and save the response to a temporary file
response_file=$(mktemp)
curl -s -o "$response_file" "$url"

# Check if curl encountered an error
if [ $? -ne 0 ]; then
    echo "Error: Unable to retrieve data from $url"
    rm -f "$response_file"
    exit 1
fi

# Get the size of the response body in bytes and display it
body_size=$(wc -c < "$response_file")
echo "$body_size"

# Clean up the temporary response file
rm -f "$response_file"
