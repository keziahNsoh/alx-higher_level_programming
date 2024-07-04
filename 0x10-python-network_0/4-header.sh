#!/bin/bash
# Script to send a GET request with a header to a URL and display the response body

url=$1

# Send GET request with header and display response body
response=$(curl -sH "X-School-User-Id: 98" "$url")

# Check if the response contains "Hello School!"
if [[ "$response" == *"Hello School!"* ]]; then
    echo "Hello School!"
else
    echo "Error: Unexpected response from server"
fi

