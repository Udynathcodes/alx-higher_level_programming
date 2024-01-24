#!/usr/bin/python3
"""
No module imported
"""


class Square:
    """
    A class that defines a square with a
    Private instance attribute: size
    """
    def __init__(self, size=0):
        """
        Args:
            size:
                if not an int, raise TypeError
                if size < 0, raise ValueError
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        A method that returns the area of the square
        size**2
        """
        return self.__size**2
