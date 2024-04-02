#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """
    function that prints x elements of a list.

    Args:
        my_list: list contain any type.
        x: number of elements to print.

    Return:
        the real number of element printed.
    """
    count = 0
    try:
        for i in range(x):
            print(f"{my_list[i]}", end="")
            count += 1
    except IndexError:
        pass
    print("")
    return count
