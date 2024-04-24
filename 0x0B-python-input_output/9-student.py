#!/usr/bin/python3
""" Student Class """


class Student:
    """
    Class that define a student.

    Attributes:
        instance:
            first_name: first name of the student
            last_name: last name of the student
            age: age of the student

    Methods:
        instance:
            __init__: initialization method
            to_json: retrieves a dictionary representation of a student.
    """
    def __init__(self, first_name, last_name, age):
        """
        initailization method for the student.

        Args:
            first_name: first name of the student
            last_name: last name of the student
            age: age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        function retrieves a dictionary representation of the Student object
        """
        return self.__dict__
