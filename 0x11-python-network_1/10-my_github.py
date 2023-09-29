#!/usr/bin/python3
"""Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id"""


import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/user"
    user_name = sys.argv[1]
    password = sys.argv[2]
    req = requests.get(url, auth=(user_name, password))
    if req.status_code == 200:
        print(req.json().get('id'))
    else:
        print("None")
