#!/usr/bin/python3
"""
 No module imported
"""


class Square:
    """
    Defines a square.

    Attributes:
    - __size (int): The size of the square.

    Methods:
    - __init__(self, size=0): Initializes a new square instance.
    - size (property): Getter method for the size property.
    - size (setter): Setter method for the size property.
    - area(self): Calculates and returns the area of the square.
    - my_print(self): Prints the square using '#' characters.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new square instance.

        Parameters:
        - size (int): The size of the square (default is 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for the size property.

        Returns:
        - int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size property.

        Parameters:
        - value (int): The new size for the square.

        Raises:
        - TypeError: If the provided value is not an integer.
        - ValueError: If the provided value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Getter method for property position

        Returns:
            The position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for position property

        :param value:
            position of the square(tuple)
            must be a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self.__size**2

    def my_print(self):
        """
        Prints the square using '#' and ' ' characters.
        If size is equal to 0, prints an empty line.
        If position[1] is equal to 0, prints nothing.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
