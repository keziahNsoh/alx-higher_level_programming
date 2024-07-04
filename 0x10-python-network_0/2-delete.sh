#!/bin/bash
# This script sends a DELETE request to the URL passed as the first argument and displays the body of the response

url=$1
response=$(curl -s -o /dev/null -w "%{http_code}" "$url")

if [[ $response -eq 200 ]]; then
    curl -sX DELETE "$url"
else
    echo "Error: Failed to DELETE $url. HTTP status code: $response"
fi

