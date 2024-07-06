#!/usr/bin/python3


"""
Response header value
Description: Python script that takes in a URL, sends a request to the URL and displays the body of the response with an error handler
"""

import urllib.request
import sys

def main():
    try:
         request_url = sys.argv[1]
         with urllib.request.urlopen(request_url) as result:
             print(result.read())
    except urllib.error.HTTPError as error:
         print("Error code: {}".format(error.code))







if __name__ == "__main__":
    main()

