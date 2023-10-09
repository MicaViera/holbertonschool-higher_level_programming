#!/usr/bin/python3
"""Write a class Square that inherits from Rectangle class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle class."""
    def __init__(self, size):
        """Initializes Square class that inherits from Rectangle class."""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Function that returns the area."""
        area = self.__size ** 2
        return area

    def __str__(self):
        return (f"[Square] {self.__size}/{self.__size}")
