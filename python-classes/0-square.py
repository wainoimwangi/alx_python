#!/usr/bin/python3


"""
Write a class Square that defines a square by:

    Private instance attribute: size
    Instantiation with size (no type/value verification)
    You are not allowed to import any module
"""


class Square:
    """
    Represents a square with a private instance attribute 'size'.

    Attributes:
        size (int): The size of the square's sides.

    Methods:
        __init__(self, size):
            Initializes a new Square object with the given size.
    """
    def __init__(self, size):
        """
        Function/ method that initializes the object size.

        Args:
            size (int): The size of the square's sides.
        """
        self._Square__size = size
