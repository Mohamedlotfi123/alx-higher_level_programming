#!/usr/bin/python3


def best_score(a_dictionary):
    """
    function returns a key with the biggest integer value.

    Args:
        a_dictionary: a dictionary.

    Return:
        the beggest integer or,
        None if no score.
    """
    if not a_dictionary:
        return None
    key = ["value"]
    value = 0
    for k, v in a_dictionary.items():
        if v > value:
            value = v
            key[0] = k
    return key[0]
