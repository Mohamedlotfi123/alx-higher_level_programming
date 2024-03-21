#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """
    function returns a new dictinary with all values
    multiplied by two.

    Args:
        a_dictionary: a dictionary.

    Return:
        New dictionary.
    """
    ndict = {}
    for k, v in a_dictionary.items():
        ndict[k] = v * 2
    return ndict
