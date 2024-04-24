#!/usr/bin/python3
""" From JSON string to object. """
import json


def from_json_string(my_str):
    """
    function that returns an object (python data structure) represented by a
    json string.

    Args:
        my_str: object to deserialize

    Return:
        Deserialize object.
    """
    return json.loads(my_str)
