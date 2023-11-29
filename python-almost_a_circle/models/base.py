#!/usr/bin/python3
"""Write the first Class Base"""
import json


class Base:
    """Base Class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Function that Initializes the class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Function that returns the JSON string of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Method that writes json string representation of list_objs."""
        Lista = []
        with open(f"{cls.__name__}.json", "w") as file:
            if list_objs is None:
                list_objs = []
            for objs in list_objs:
                Lista.append(objs.to_dictionary())
            file.write(cls.to_json_string(Lista))

    @staticmethod
    def from_json_string(json_string):
        """Metho  that returns a list of the JSON string representation"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Method that returns an instance with attributes."""
