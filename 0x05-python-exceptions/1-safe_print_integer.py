#!/usr/bin/python3


def safe_print_integer(value):
    """
    function prints an integer.

    Args:
        value: can be any type.

    Return:
        True if the value is correctly printed, or False otherwise.
    """
    if not value:
        return False
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
