#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """
    function replace element of a list at specific position.

    Args:
        my_list: list to replace in.
        idx: index of the element to replace.
        element: repalce value.

    Return:
        New list or,
        None if idx is negative or out of range.
    """
    if idx < 0 or idx >= len(my_list):
        return None
    my_list[idx] = element
    return my_list
