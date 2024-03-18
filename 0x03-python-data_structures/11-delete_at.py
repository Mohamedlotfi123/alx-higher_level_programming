#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    """
    function delete the item at a specific position in a list.

    Args:
        my_list: list of items.
        idx: index to delete the item in it.

    Return:
        new_list after the deletion or,
        the original list if idx is negative or out of range.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    del my_list[idx]
    return my_list
