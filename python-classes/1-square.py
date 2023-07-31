#!/usr/bin/python3


"""
Write a class Square that defines a square by: (based on 0-square.py)

Private instance attribute: size
Instantiation with optional size: def __init__(self, size=0):
size must be an integer, otherwise raise a TypeError exception with the message size must be an integer
if size is less than 0, raise a ValueError exception with the message size must be >= 0
You are not allowed to import any module
"""


class Square:
    """
    Represents a square with a private instance attribute 'size'.

    Attributes:
        size (int): The size of the square's sides.

    Methods:
        __init__(self, size = 0):
            Initializes a new Square object with the given size.
    """
    def __init__(self, size = 0):
        """
        Initializes a Square instance.

        Args:
            size (int, optional): The size of the square (default is 0).

        Raises:
            TypeError: If the provided size is not an integer.
            ValueError: If the provided size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("Input must be an integer")
        if size < 0:
            raise ValueError("The input value must be a positive value")
        self._Square__size = size
