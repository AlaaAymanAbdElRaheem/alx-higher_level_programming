#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except ZeroDivisionError as err:
        result = None
        sys.stderr.write("Exception: " + str(err) + "\n")
    except IndexError as err:
        result = None
        sys.stderr.write("Exception: " + str(err) + "\n")
    return result
