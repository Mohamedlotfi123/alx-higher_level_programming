#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    """
    function deletes a key in a dictionary.

    Args:
        a_dictionary: a dictionary.
        key: key of the value to delete.

    Return:
        dictionary after deletion.
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
