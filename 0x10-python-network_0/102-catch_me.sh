#!/bin/bash
# Script that makes a request to 0.0.0.0:5000/catch_me and causes the server to respond with "You got me!"

# Send a PUT request to the specific URL with the appropriate options to trigger the desired response
curl -s -X PUT -L -d "user_id=98" -H "Origin: HolbertonSchool" "0.0.0.0:5000/catch_me"

