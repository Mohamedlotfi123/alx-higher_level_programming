#!/usr/bin/python3
""" Base Class """
import json
import csv


class Base():
    """
    Base class.

    Attributes:
        class:
            __nb_objects: ...
        instance:
            id: id of the instance.
    methods:
        __init__: initialization method.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialization method.

        Args:
            id: id of the instance.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        function that returns JSON representation of list_dictionaries.

        Args:
            list_dictionaries: list of dictionaries.

        Return:
            JSON representation of list_dictionaries, or
                "[]" if list_dictionaries is None.
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        function write JSON string to a file.

        Args:
            list_objs: list of instances who inherits of Base.
        """
        dict_list = list()
        if list_objs is not None:
            for obj in list_objs:
                dict_list.append(obj.to_dictionary())
        json_format = cls.to_json_string(dict_list)
        with open(f"{cls.__name__}.json", "w") as f:
            f.write(json_format)

    @staticmethod
    def from_json_string(json_string):
        """
        function returns list of the JSON string representation

        Args:
            json_string: string representation list of dictionries.

        Return:
            list of dictionaries, or empty list if
                json_string is None
        """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        function returns an instance with all attributes already set.

        Args:
            dictionary: dictionary with attributes values.
        """
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        else:
            instance = cls(1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """
        function that returns a list of instaces.
        """
        obj_list = list()
        try:
            with open(f"{cls.__name__}.json", "r") as f:
                json_string = f.read()
        except FileNotFoundError:
            return obj_list
        dict_list = cls.from_json_string(json_string)
        for dic in dict_list:
            instance = cls.create(**dic)
            obj_list.append(instance)
        return obj_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        function that serializes in CSV

        Args:
            list_objs: list of objects
        """
        dict_list = list()
        if list_objs is not None:
            for obj in list_objs:
                obj_dict = obj.to_dictionary()
                dict_list.append(obj_dict.values())
        with open(f"{cls.__name__}.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(dict_list)

    @classmethod
    def load_from_file_csv(cls):
        """
        function deserializes from CSV.
        """
        list_obj = list()
        try:
            with open(f"{cls.__name__}.csv", "r") as f:
                reader = csv.reader(f)
                values_list = list(reader)
        except FileNotFoundError:
            return list_obj
        for values in values_list:
            if cls.__name__ == "Rectangle":
                attr_list = ["id", "__width", "__height", "__x", "__y"]
                instance = cls(1, 1)
            else:
                attr_list = ["id", "__size", "__x", "__y"]
                instance = cls(1)
            for i, value in enumerate(values):
                setattr(instance, attr_list[i], value)
            list_obj.append(instance)
        return list_obj
