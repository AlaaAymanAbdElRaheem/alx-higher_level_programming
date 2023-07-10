#!/usr/bin/python3
"""defining add_attribute function"""


def add_attribute(obj, attr_name, value):
    """implement add_attribute function"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, value)
