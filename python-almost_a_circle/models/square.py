#!/usr/bin/python3
"""Write the class Square that inherits from Rectangle"""
from .rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from class Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Function that initializes the class."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Function that returns a string."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Method that assigns a argument to each attribute."""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for kw, value in kwargs.items():
                if kw == "id":
                    self.id = value
                if kw == "size":
                    self.size = value
                if kw == "x":
                    self.x = value
                if kw == "y":
                    self.y = value

    def to_dictionary(self):
        """Method that cretaes a dictionary."""
        Square = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
        return Square
