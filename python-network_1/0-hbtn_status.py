#!/usr/bin/python3
"""
This is a Python script that fetches https://alu-intranet.hbtn.io/status

Uses the package requests
"""
import requests

request = requests.get("https://alu-intranet.hbtn.io/status")

if response.status_code == 200:
    data = response.json()
    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
else:
    print("Error: Unable to fetch data. Status code: {}".format(response.status_code))