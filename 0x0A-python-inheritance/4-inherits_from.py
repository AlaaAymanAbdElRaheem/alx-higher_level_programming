#!/usr/bin/python3
"""defining inherits_from function"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that inherited"""
    if issubclass(obj.__class__, a_class) and type(obj) is not a_class:
        return True
    return False
