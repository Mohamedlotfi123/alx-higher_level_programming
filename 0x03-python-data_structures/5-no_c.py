#!/usr/bin/python3


def no_c(my_string):
    """
    function removes all characters c and C from a string.

    Args:
        my_string: string to remove from.

    Return:
        New string.
    """
    new_string = ""
    for char in my_string:
        if char in ["c", "C"]:
            continue
        new_string = new_string + char
    return new_string
