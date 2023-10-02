#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square:
    """Square Class"""
    def __init__(self, size=0):
        """Initializing Square Function"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """Area of a Square Function"""
        area = self.__size * self.__size
        return area
