#!/usr/bin/python3
"""Write an empty class Rectangle that defines a rectangle"""


class Rectangle:
    """Rectangle Class."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        print_rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for h_element in range(self.__height):
                for w_element in range(self.__width):
                    print_rectangle += "#"
                print_rectangle += "\n"
            return print_rectangle[:-1]

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
