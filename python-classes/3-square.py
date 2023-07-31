#!/usr/bin/python3


"""
Write a class Square that defines a square by: (based on 1-square.py)

Private instance attribute: size
Instantiation with optional size: def __init__(self, size=0):
Raise a TypeError exception with the message size must be an integer
Raise a ValueError exception with the message size must be >= 0
Public instance method: def area(self): returns the current square area
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

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size

    def area(self):
        """
        Calculates the area of the square and returns the area.
        """
        return self._Square__size ** 2

    def size(self):
        """
        Retrieves the size of the square.
        """
        return self._Square__size
 
    def size(self, value):
        """
        Sets the size of the square to value.

        Args:
            value (int): The new size for the square.

        Raises:
            TypeError: If the provided new_size is not an integer.
            ValueError: If the provided new_size is less than 0.
        """ 
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value    
