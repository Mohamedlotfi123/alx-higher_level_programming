#!/usr/bin/python3
""" Mylist Class """


class MyList(list):
    """ Mylist class that inherits from list class. """

    def print_sorted(self):
        """ print the list in ascending order. """
        mylist = sorted(self.copy())
        print(mylist)
