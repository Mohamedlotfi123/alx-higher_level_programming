#!/usr/bin/python3


def print_list_integer(my_list=[]):
    """
    function prints all integers of a list.

    Args:
        my_list: list to print it's integers.
    """
    for i in my_list:
        print("{:d}".format(i))
