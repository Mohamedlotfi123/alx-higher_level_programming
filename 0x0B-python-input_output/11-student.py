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
            reload_from_json: replaces all attributes of hte student
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

    def to_json(self, attrs=None):
        """
        function retrieves a dictionary representation of the Student object

        Args:
            attrs: list contain the name of attributes to retrieve
        """
        if attrs is not None:
            my_dict = {}
            for key in self.__dict__:
                if key in attrs:
                    my_dict[key] = self.__dict__[key]
            return my_dict
        return self.__dict__

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student.

        Args:
            json: dictionary it's keys is attributes name and
                  values is new value for the attribute.
        """
        for key in json:
            self.__dict__[key] = json[key]
