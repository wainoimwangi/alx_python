#!/usr/bin/python3
"""
    This is a base class
"""

class BaseGeometry:
    """
    This is a base class
    """


    def area(self):
        """
        Function that raise an exception with an error message
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Function validates whether the value is an integer and
        is greater than 0, otherwise it raises an error
        """
        self.name = name
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.value = value