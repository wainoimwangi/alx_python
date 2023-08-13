#!/usr/bin/python3
"""
This is a Python script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.

The letter is sent in the variable q
If no argument is given, q=""
If the response body is properly JSON formatted and not empty,
display the id and name like this: [<id>] <name>
Otherwise:
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty
You must use the package requests and sys
"""
import requests
import sys

def main():
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    parameter = {'q': q}
    response = requests.post(url, data=parameter)

    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No Result")
    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    main()
