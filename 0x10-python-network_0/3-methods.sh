#!/bin/bash
# Script to determine allowed HTTP methods for a given URL using curl

url=$1

# Function to check if method is allowed
check_method() {
    local url=$1
    local method=$2

    # Send request and capture response code
    response_code=$(curl -s -o /dev/null -w "%{http_code}" -X "$method" "$url")

    # Check if response code indicates method is allowed
    if [ "$response_code" -eq 200 ] || [ "$response_code" -eq 204 ]; then
        echo "$method"
    fi
}

# Array of HTTP methods to check
methods=("OPTIONS" "GET" "HEAD" "POST" "PUT" "DELETE" "PATCH")

# Iterate over methods and check each one
allowed_methods=""
for method in "${methods[@]}"; do
    result=$(check_method "$url" "$method")
    if [ -n "$result" ]; then
        allowed_methods+=" $result"
    fi
done

# Output allowed methods
if [ -z "$allowed_methods" ]; then
    echo "Error: Could not determine allowed HTTP methods for $url"
else
    echo "$allowed_methods"
fi

