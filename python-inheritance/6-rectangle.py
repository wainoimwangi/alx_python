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
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        self.value = value

class Rectangle(BaseGeometry):
    """
    This is a sub-class of the baseclass
    """
    def __init__(self, width, height):
        """
        function sets the values width and height and ensures
        """
        self.integer_validator("width", width)
        self._Rectangle__width = width
        self.integer_validator("height", height)
        self._Rectangle__height = height

    def __str__(self):
        return f"Rectangle(width={self._Rectangle__width}, height={self._Rectangle__height})"