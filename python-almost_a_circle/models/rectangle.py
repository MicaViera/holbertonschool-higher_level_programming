#!/usr/bin/python3
"""Write the class Rectangle that inherits from Base."""
from .base import Base


class Rectangle(Base):
    """Class Rectangle inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Function that returns the area of the rectangle."""
        area = self.__height * self.__width
        return area

    def display(self):
        """Function that displays the rectangle in stdout."""
        for y_element in range(self.__y):
            print()
        for h_element in range(self.__height):
            for x_element in range(self.__x):
                print(" ", end="")
            for w_element in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Function that returns a string."""
        return f"[Rectangle] ({self.id}) {self.__x}\
/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Method that assigns a argument to each attribute."""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        else:
            for kw, value in kwargs.items():
                if kw == "id":
                    self.id = value
                if kw == "width":
                    self.__width = value
                if kw == "height":
                    self.__height = value
                if kw == "x":
                    self.__x = value
                if kw == "y":
                    self.__y = value
