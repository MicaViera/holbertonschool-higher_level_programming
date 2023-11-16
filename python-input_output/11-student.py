#!/usr/bin/python3
"""Write a class Student."""


class Student:
    """Student class."""

    def __init__(self, first_name, last_name, age):
        """Method that initializes the class."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Method that retrieves a dictionary representation."""
        if isinstance(attrs, list):
            dictionary = {}
            for item in attrs:
                if item in self.__dict__:
                    dictionary[item] = self.__dict__[item]
            return dictionary
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Method that replaces of Student instance."""
        for key, value in json.items():
            setattr(self, key, value)
