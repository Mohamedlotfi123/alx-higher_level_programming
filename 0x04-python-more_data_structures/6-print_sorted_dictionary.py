#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """
    function prints a dictionary by ordered keys.

    Args:
        a_dicrionaty: dictionaty to print.
    """
    list_of_keys = list(a_dictionary)
    for key in sorted(list_of_keys):
        print(f"{key}: {a_dictionary[key]}")
