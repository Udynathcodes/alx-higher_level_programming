#!/usr/bin/python3
"""Modules imported"""
import json
from models.base import Base


class Rectangle(Base):
    """
    Represents a Rectangle, a subclass of the Base class.

    Attributes:
    - __width (int): Width of the rectangle.
    - __height (int): Height of the rectangle.
    - __x (int): X-coordinate of the top-left corner of the rectangle.
    - __y (int): Y-coordinate of the top-left corner of the rectangle.
    - id (int): Identifier of the rectangle (inherited from the Base class).

    Methods:
    - __init__(self, width, height, x=0, y=0, id=None): Constructor
    to initialize a Rectangle instance.
    - width (property): Getter for the width attribute.
    - width (setter): Setter for the width attribute.
    - height (property): Getter for the height attribute.
    - height (setter): Setter for the height attribute.
    - x (property): Getter for the x attribute.
    - x (setter): Setter for the x attribute.
    - y (property): Getter for the y attribute.
    - y (setter): Setter for the y attribute.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Parameters:
        - width (int): Width of the rectangle.
        - height (int): Height of the rectangle.
        - x (int): X-coordinate of the top-left corner of the rectangle.
        - y (int): Y-coordinate of the top-left corner of the rectangle.
        - id (int): Identifier of the rectangle (inherited from the Base
        class).
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Getter for the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attribute."""
        if value < 0:
            raise ValueError("x must be >= 0")
        elif not isinstance(value, int):
            raise TypeError("x must be an integer")
        else:
            self.__x = value

    @property
    def y(self):
        """Getter for the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y attribute."""
        if value < 0:
            raise ValueError("y must be >= 0")
        elif not isinstance(value, int):
            raise TypeError("y must be an integer")
        else:
            self.__y = value

    def area(self):
        """A public method that returns the area
        value of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """
        A public method that
        prints in stdout the Rectangle instance
        with the character # and returns the string
        generated
        """
        result = ""
        for i in range(self.__height):
            char_rect = "#" * self.__width
            result += char_rect + "\n"
            print(char_rect)
        return result

    def __str__(self):
        """Rectangle __str__ method(overriding)"""
        return "[{}] ({}) {}/{} - {}/{}".format(
            (type(self).__name__), self.id, self.x, self.y,
            self.width, self.height
        )

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
        return "[{}] ({}) {}/{} - {}/{}".format(
            (type(self).__name__), self.id, self.width, self.height,
            self.x, self.y)

    def to_dictionary(self):
        """Returns a dictonary representation of Rectangle"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}

