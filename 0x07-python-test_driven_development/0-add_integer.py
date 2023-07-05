#!/usr/bin/python3
"""definies add_integer function"""


def add_integer(a=0, b=98):
    """adds two integers"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
