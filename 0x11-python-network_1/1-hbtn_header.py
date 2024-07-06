#!/usr/bin/python3


"""
Response header value
Description: Prints script that takes,sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response
"""

import urllib.request
import sys

def main():
   request_url = sys.argv[1]
   with urllib.request.urlopen(request_url) as result:
     header = result.getheader('X-Request-Id')
     print(header)







if __name__ == "__main__":
   main()

