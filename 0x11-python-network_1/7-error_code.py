#!/usr/bin/python3


"""
Response header value
Description: Python script that takes in a URL, sends a request to the URL and displays the body of the response with an error handler
"""

import sys
import requests

def main():
   try:
      request_url = sys.argv[1]
      result = requests.get(request_url)
      result.raise_for_status()
      print(result.text)
   except requests.exceptions.HTTPError as error:
      print(error.response.status_code)







if __name__ == "__main__":
   main()

