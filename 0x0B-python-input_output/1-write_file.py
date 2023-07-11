#!/usr/bin/python3
"""defining write_file function"""


def write_file(filename="", text=""):
    """implement write_file function"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
