#!/usr/bin/python3


def element_at(my_list, idx):
    """
    function retrieves an element from a list.

    Args:
        my_list: list to retrieves from.
        idx: index of the element to retrieve.

    Return:
        element at idx or,
        None if idx is negative or out of range.
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
