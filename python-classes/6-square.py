#!/usr/bin/python3
"""Write a class Square that defines a square."""


class Square:
    """Square Class"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializing Square Function."""
        self.__size = size
        self.__position = position

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
        """Area of a Square Function."""
        area = self.__size * self.__size
        return area

    def my_print(self):
        """Method that prints #."""
        if self.__size == 0:
            print()
            return None
        for space in range(self.__position[1]):
            print()
        for element in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    @property
    def position(self):
        """Method that retrieves position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Method for the position."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for idx in value:
            if not isinstance(idx, int) or idx <= 0:
                raise TypeError("position must be a tuple\
 of 2 positive integers")
        self.__position = value
