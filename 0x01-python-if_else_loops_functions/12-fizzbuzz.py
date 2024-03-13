#!/usr/bin/python3


def fizzbuzz():
    """
    Function prints from 1 to 100, and if the number is multiple of
    3 print fizz or multiple of 5 ptint buzz, and if multiple of both
    print fizzbuzz.

    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
