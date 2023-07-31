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

    Note:
        - The 'size' attribute is a private instance attribute, denoted by the double underscore prefix.
        - The class does not perform any type or value verification on the 'size' attribute during instantiation.
        - No external modules are used or imported for the implementation of this class.
    """
    def __init__(self, size):
        """
        Function/ method that initializes the object size and returns the value size.
        
        Args:
            size (int): The size of the square's sides.
        """
        self.size = size




