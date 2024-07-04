#!/bin/bash
# Script that sends a JSON POST request to a URL passed as the first argument,
# and displays the body of the response.

# Function to check if a file contains valid JSON
function is_valid_json() {
    file="$1"
    if jq -e . "$file" >/dev/null 2>&1; then
        return 0 # Valid JSON
    else
        return 1 # Not a valid JSON
    fi
}

# Check if exactly two arguments are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <URL> <filename>"
    exit 1
fi

# Extract arguments
url="$1"
file="$2"

# Check if file exists
if [ ! -f "$file" ]; then
    echo "File '$file' not found"
    exit 1
fi

# Validate JSON content
if is_valid_json "$file"; then
    echo "Valid JSON"
else
    echo "Not a valid JSON"
    exit 1
fi

# Send POST request with JSON content in file
curl -s -X POST -H "Content-Type: application/json" -d @"$file" "$url"

