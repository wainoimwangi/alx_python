#!/usr/bin/python3
"""
This is a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id

Uses Basic Authentication with a personal access token as password
to access to your information (only read:user permission is needed)
The first argument is the username
The second argument is the password
(in your case, a personal access token as password)
Uses the package requests and sys
"""
import requests
import sys

def main():
    username = sys.argv[1]
    access_token = sys.argv[2]

    url = "https://api.github.com/user"
    headers = {
        "Authorization": f"Basic {username}:{access_token}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data.get("id")
        if user_id is not None:
            print("Your GitHub user ID:", user_id)
        else:
            print("User ID not found in response.")
    else:
        print("Error fetching user data. Status code:", response.status_code)

if __name__ == "__main__":
    main()
