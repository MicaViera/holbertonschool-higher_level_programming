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
