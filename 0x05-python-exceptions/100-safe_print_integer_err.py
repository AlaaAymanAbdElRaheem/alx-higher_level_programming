#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print('{:d}'.format(value))
        return True
    except TypeError as err:
        sys.stderr.write("Exception: " + str(err) + "\n")
        return False
    except ValueError as err:
        sys.stderr.write("Exception: " + str(err) + "\n")
        return False