#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """
    function that replace an element in a list at a specific postision
    without modifying the original list.

    Args:
        my_list: list to replace in without modifying it.
        idx: index of the element to modify.
        element: value to modify with.

    Return:
        modified list or,
        copy of the original list if idx is negative or out of range.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    new_list = my_list[:]
    new_list[idx] = element
    return new_list
