#!/usr/bin/python3
"""Write an empty class BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inherits from BaseGeometry class."""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Function that returns the area."""
        area = self.__height * self.__width
        return area
    
    def __str__(self):
        return (f"[Rectangle] {self.__width}/{self.__height}")
