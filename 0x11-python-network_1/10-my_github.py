#!/usr/bin/python3


"""
Response header value
Description: a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.
"""

import sys
import requests

def main():
   q = ""
   if sys.argv[1]:
      q = sys.argv[1]
   try:
      result = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
      data = result.json()
      print(data)
      if not data:
         print("No result")
      else:
         print("[{}] {}".format(data.get("id"), data.get('name')))
   except requests.exceptions.JSONDecodeError as error:
      print("Not a valid JSON")




if __name__ == "__main__":
   main()

