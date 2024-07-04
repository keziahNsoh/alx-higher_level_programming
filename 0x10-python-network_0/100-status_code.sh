#!/bin/bash
# Script that sends a request to a URL passed as an argument and displays only the status code of the response

# Check if exactly one argument (URL) is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Attempt to retrieve HTTP status code with curl and store the output
http_code=$(curl -s -o /dev/null -w "%{http_code}" "$1")

# Extract only the HTTP status code from curl output
echo "$http_code" | grep -o '[0-9]*'

