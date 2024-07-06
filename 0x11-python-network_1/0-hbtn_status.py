#!/usr/bin/python3
"""
What's my status
Description: This module fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request

def main():
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as result:
    response_body = result.read()
    response_type = type(response_body)
    response_content = response_body
    utf8_content = response_body.decode('utf-8')

    #Display of the body of the response,response_type, response_content and response_type, response_content

    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".format(response_type, response_content, utf8_content))



if __name__ == "__main__":
    main()

