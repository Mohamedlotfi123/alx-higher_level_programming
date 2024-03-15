#!/usr/bin/python3
from sys import argv


def main():
    if len(argv) == 1:
        print(0)
    else:
        i = 1
        result = 0
        while i < len(argv):
            result += int(argv[i])
            i += 1
        print(result)


if __name__ == "__main__":
    main()
