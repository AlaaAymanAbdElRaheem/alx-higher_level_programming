#!/usr/bin/python3
"""defining append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """insert line of text to a file, after each line with a specific string"""
    with open(filename, 'r', encoding="utf-8") as f:
        data_list = f.readlines()

    new_data = []
    for line in data_list:
        new_data.append(line)
        if search_string in line:
            new_data.append(new_string)

    with open(filename, 'w', encoding="utf-8") as f:
        for line in new_data:
            f.write(line)
