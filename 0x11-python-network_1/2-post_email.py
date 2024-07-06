#!/usr/bin/python3


"""
Response header value
Description: A Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response
"""

import urllib.request
import sys

def main():
   request_url = sys.argv[1]
   email = sys.argv[2]
   data = urllib.parse.urlencode({"email": email})
   with urllib.request.urlopen(request_url, data.encode('ascii')) as result:
      print(result.read().decode('utf-8'))






if __name__ == "__main__":
   main()

