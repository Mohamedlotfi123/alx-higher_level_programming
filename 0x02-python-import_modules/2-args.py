#!/usr/bin/python3
from sys import argv


def main():
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) >= 2:
        if len(argv) == 2:
            print("1 argument:")
        else:
            print("{} arguments:".format(len(argv) - 1))
        i = 1
        while i < len(argv):
            print("{}: {}".format(i, argv[i]))
            i += 1


if __name__ == "__main__":
    main()
