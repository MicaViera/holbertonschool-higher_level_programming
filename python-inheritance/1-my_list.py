#!/usr/bin/python3
"""Write a class MyList that inherits from list."""


class MyList(list):
    """My List Class."""

    def print_sorted(self):
        """Function that prints a list."""
        sort = sorted(self)
        return print(sort)
