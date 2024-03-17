#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """
    function prints a matrix of integers.

    Args:
        matrix: matrix to print.
    """
    for row in matrix:
        for element in row:
            print("{:d}".format(element), end=" ")
        print()
