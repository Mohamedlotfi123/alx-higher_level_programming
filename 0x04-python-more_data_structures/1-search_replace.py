#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """
    function that replace all occurrences of an element by
    another in a new list.

    Args:
        my_list: initial list.
        search: element to raplace in the list.
        repalce: new element.

    Return:
        new list with the replacement.
    """
    nlist = []
    for value in my_list:
        if value == search:
            nlist.append(replace)
        else:
            nlist.append(value)
    return nlist
