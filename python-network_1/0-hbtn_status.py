#!/usr/bin/python3
"""
This is a Python script that fetches https://alu-intranet.hbtn.io/status

Uses the package requests
"""
import requests

def check_status(url):
    """
    Fetches the status from the given URL and displays the response body.

    Args:
        url (str): The URL to fetch the status from.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        context = response.text

        print("Body response:")
        print("\t- type:", type(context))
        print("\t- content:", context)

    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)

if __name__ == "__main__":
    fetch_url = "https://alu-intranet.hbtn.io/status"
    check_status(fetch_url)