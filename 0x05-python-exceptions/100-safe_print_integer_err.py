#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """
    function that prints an integer.

    Args:
        value: any type.

    Return:
        True if value has been correctly printed (value is integer),
        or otherwise False.
    """
    try:
        print("{:d}".format(value))
        return True
    except ValueError as v:
        print("Exception:", v, file=sys.stderr)
        return False
    except TypeError as t:
        print("Exception:", t, file=sys.stderr)
        return False
