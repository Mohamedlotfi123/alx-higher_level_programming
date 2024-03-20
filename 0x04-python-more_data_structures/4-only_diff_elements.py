#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """
    function returns set of all elements present in only one set.

    Args:
        set_1: first set of elements.
        set_2: second set of elements.

    Return:
        set of all elements present in only one set.
    """
    return set_1 ^ set_2
