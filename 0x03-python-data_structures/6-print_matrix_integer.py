#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """
    function prints a matrix of integers.

    Args:
        matrix: matrix to print.
    """
    for row in matrix:
        for element in row:
            if row.index(element) != len(row) - 1:
                print("{:d}".format(element), end=" ")
            else:
                print("{}".format(element), end="")
        print()
