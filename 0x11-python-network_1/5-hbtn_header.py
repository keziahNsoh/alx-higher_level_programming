#!/usr/bin/python3


"""
Response header value
Description: a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header
"""

import sys
import requests

def main():
   url = sys.argv[1]
   result = requests.get(url)
   print(result.headers['X-Request-Id'])






if __name__ == "__main__":
   main()

