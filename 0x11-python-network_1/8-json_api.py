#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""


import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""

    data = {'q': q}
    req = requests.post(url, data=data)
    try:
        json_format = req.json()
        if json_format:
            print("[{}] {}".format(
                json_format.get('id'), json_format.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
