#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    """
    function adds two tuples.

    Args:
        tuple_a: first tuple.
        tuple_b: second tuple.

    Return:
        tuple with 2 integers.
    """
    my_list = []
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    for i in range(2):
        if i > len(list_a) - 1:
            list_a.append(0)
        if i > len(list_b) - 1:
            list_b.append(0)
        my_list.append(list_a[i] + list_b[i])
    return tuple(my_list)
