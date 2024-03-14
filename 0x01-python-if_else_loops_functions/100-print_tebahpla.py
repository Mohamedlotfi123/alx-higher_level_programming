#!/usr/bin/python3


def main():
    """
    Program that print the ASCII alphabet in reverse.

    """
    for char in range(122, 96, -1):
        if char % 2 != 0:
            char = char - 32
        print(chr(char), end="")


main()
