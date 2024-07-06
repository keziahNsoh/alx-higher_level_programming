#!/usr/bin/python3


"""
Response header value
Description: A Python script that fetches https://alx-intranet.hbtn.io/status with requests
"""

import requests

def main():
    result = requests.get("https://alx-intranet.hbtn.io/status")
    response_content = result.text
    response_type = type(response_content)
    print("Body response:\n\t- type: {}\n\t- content: {}".format(response_type, response_content))







if __name__ == "__main__":
    main()

