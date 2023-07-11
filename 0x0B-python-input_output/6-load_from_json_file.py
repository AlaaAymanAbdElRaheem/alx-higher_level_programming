#!/usr/bin/python3
"""defining load_from_json_file function"""


import json


def load_from_json_file(filename):
    """implement load_from_json_file function"""
    with open(filename) as f:
        data = json.load(f)
    return data
