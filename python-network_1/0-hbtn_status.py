#!/usr/bin/python3
"""
This is a Python script that fetches https://alu-intranet.hbtn.io/status

Uses the package requests
"""
import requests

def fetch_and_display_status(url):
    """
    Fetches the status from the given URL and displays the response body.

    Args:
        url (str): The URL to fetch the status from.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        content = response.text

        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    status_url = "https://alu-intranet.hbtn.io/status"
    fetch_and_display_status(status_url)