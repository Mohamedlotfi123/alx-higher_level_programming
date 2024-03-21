#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    """
    function replaces or adds key/value in a dictionary.

    Args:
        a_dictionary: dictionary.
        key: key to the value in a dictionary.
        value: value of the key in a dictionary.

    Returns:
        New dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
