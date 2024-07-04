#!/bin/bash
# This script sends a POST request with parameters email and subject

# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Variables for POST data
url=$1
email="test@gmail.com"
subject="I will always be here for PLD"

# Print POST params header and values
echo "POST params:"
echo "    email: $email"
echo "    subject: $subject"

# Send POST request with curl and display response body
curl -s -X POST "$url" -d "email=$email" -d "subject=$subject" | cat

echo ""  # For proper formatting in the output

