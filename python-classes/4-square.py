#!/usr/bin/python3


"""
Write a class Square that defines a square by: (based on 3-square.py)

Private instance attribute: size:
    property def size(self): to retrieve it
    property setter def size(self, value): to set it:
        Raise a TypeError exception with the message size must be an integer
        Raise a ValueError exception with the message size must be >= 0
Instantiation with optional size: def __init__(self, size=0):
Public instance method: def area(self): that returns the current square area
Public instance method: def my_print(self): that prints in stdout the square with the character #:
    if size is equal to 0, print an empty line
You are not allowed to import any module
"""


class Square:
    """
    Represents a square with a private instance attribute 'size'.

    Attributes:
        size (int): The size of the square's sides.

    Methods:
        __init__(self, size=0):
            Initializes a new Square object with the given size.
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int, optional): The size of the square (default is 0).
        """
        self._Square__size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.
        """
        return self._Square__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square to value.

        Args:
            value (int): The new size for the square.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    def area(self):
        """
        Calculates the area of the square and returns the area.
        """
        return self._Square__size ** 2

    def my_print(self):
        """
        Prints the square using the character '#'
        when the size is equal to 0, print a new line 
        """
        if self._Square__size == 0:
            print("\n")
        else:
            for i in range(self._Square__size):
                print("#" * self._Square__size)
