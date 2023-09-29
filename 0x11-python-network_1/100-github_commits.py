#!/usr/bin/python3
"""Python script that takes 2 arguments in order to solve this challenge.
The first argument will be the repository name
The second argument will be the owner name"""


import requests
import sys

if __name__ == "__main__":
    req = requests.get('https://api.github.com/repos/{}/{}/commits'.format(
        sys.argv[2], sys.argv[1]))
    content = req.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                content[i]["sha"],
                content[i]["commit"]["author"]["name"]
            ))
    except IndexError:
        pass
