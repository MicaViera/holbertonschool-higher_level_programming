#!/usr/bin/python3
"""Write an empty class Rectangle that defines a rectangle"""


class Rectangle:
    """Rectangle Class."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        area = self.__height * self.__width
        return area

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        else:
            perimeter = (self.__height * 2) + (self.__width * 2)
        return perimeter

    def my_print(self):
        if self.__width == 0 or self.__height == 0:
            return str()
        else:
            for element in range(self.area):
                print("#" * self.area)
