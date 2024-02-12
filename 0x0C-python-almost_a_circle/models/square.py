#!/usr/bin/python3
"""Modules imported"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class, a subclass of Rectangle, represents
    a square with equal side lengths.

    Attributes:
    - size (int): The side length of the square.
    - x (int): X-coordinate of the top-left corner.
    - y (int): Y-coordinate of the top-left corner.
    - id (int): The identifier for the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new square instance.

        Parameters:
        - size (int): The side length of the square.
        - x (int): X-coordinate of the top-left corner.
        - y (int): Y-coordinate of the top-left corner.
        - id (int): The identifier for the square.
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Square __str__ method"""
        return "[{}] ({}) {}/{} - {}".format(
            (type(self).__name__), self.id, self.x, self.y,
            self.size)

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
        return "[{}] ({}) {}/{} - {}".format(
            (type(self).__name__), self.id, self.x, self.y,
            self.size)

    def to_dictionary(self):
        """Returns a dictonary representation of square"""
        return {'id': self.id, 'x': self.x,
                'size': self.size, 'y': self.y}
