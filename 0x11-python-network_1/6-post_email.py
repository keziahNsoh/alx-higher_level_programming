#!/usr/bin/python3


"""
Response header value
Description: a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.
"""

import sys
import requests

def main():
   url = sys.argv[1]
   email = sys.argv[2]
   result = requests.post(url, data={"email": email})
   print(result.text)





if __name__ == "__main__":
   main()

