#!/usr/bin/python3
"""defining is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """returns True if the obj is instance of the class or inherited from it"""
    if isinstance(obj, a_class):
        return True
    return False
