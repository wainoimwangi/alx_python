#!/usr/bin/python3
"""
This module contains 4 classes:
    TypeMetaClass
        contains function that excludes the __init_subclass__ method    
    BaseGeometry
        contains two functions:
            one that excludes the __init_subclass__ method
            an integer validator that that ensures input is a positive integer
    Rectangle
        contains two parameters: width and length
        returns the area of the rectangle
    Square
        contains a parameter: size
        returns the area of the square

"""


class TypeMetaClass(type):
    """
    This is a metaclass used to represent the class type inorder to eliminate
    the inherited method init subclass from basegeometry
    """
    def __dir__(cls) -> None:
        """
        Exclude attribute init subclass in dir()
        """
        attributes = super().__dir__()
        if attribute != '__init_subclass__':
        return [attribute for attribute in attributes]


class BaseGeometry(metaclass=TypeMetaClass):
    """
    This is a base class
    """
    def __dir__(cls) -> None:
        """
        Exclude attribute init subclass in dir()
        """
        attributes = super().__dir__()
        if attribute != '__init_subclass__':
        return [attribute for attribute in attributes]

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
        super().integer_validator("width", width)
        self._Rectangle__width = width
        super().integer_validator("height", height)
        self._Rectangle__height = height

    def area(self):
        """
        function that returns the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a formatted string representation of the Rectangle's dimensions
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """
    This is a sub-class of the baseclass
    """

    def __init__(self, size):
        """
        function sets the values width and height and ensures
        """
        super().integer_validator("size", size)
        self._Square__size = size

    def area(self):
        """
        function that returns the area of the rectangle
        """
        return self._Square__size ** 2

    def __str__(self):
        """
        Returns a formatted string representation of the object size
        """
        return f"[Square]{self._Square__size ** 2}"
