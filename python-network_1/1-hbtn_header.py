#!/usr/bin/python3
"""
This is a Python script that takes in a URL, sends a request to the URL 
and displays the value of the variable X-Request-Id in the response header

You must use the packages requests and sys
The value of this variable is different for each request
"""
import requests
import sys

def check_request_id(url):
    """
    Fetches the X-Request-Id variable from the response header of the given URL.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()

        x_request_id = response.headers.get('X-Request-Id')

        if x_request_id:
            print("{}".format(x_request_id))
        else:
            print("None")

    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <url>")
    else:
        url = sys.argv[1]
        check_request_id(url)