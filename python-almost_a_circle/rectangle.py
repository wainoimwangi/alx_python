#!/usr/bin/python3
"""
    This is a base class
"""
Base = __import__('base').Base

class Rectangle(Base):
    """
    Rectangle class that contains private instance
    variables: width, height, x and y
    """
    __width -> width
    __height -> height
    __x -> x
    __y -> y
    def __init__(self, width, height, x=0, y=0, id=None):
       """
       function that assigns variables arguments
       """
       super().__init__(id)
       self.__width = width
       self.__height = height
       self.__x = x
       self.__y = y
# width
@property
def width(self):
    """
    A getter for width
    """
    return self.__width

@width.setter
def width(self, value):
    """
    A setter for width
    """
    if value <= 0:
        raise ValueError("Must be a positive value")
        self.__width = value

# height
@property
def height(self):
    """
    A getter for height
    """
    return self.__height

@height.setter
def height(self, value):
    """
    A setter for height
    """
    if value <= 0:
        raise ValueError("Must be a positive value")
        self.__height = value

# x
@property
def x(self):
    """
    A getter for x
    """
    return self.__x

@x.setter
def x(self, value):
    """
    A setter for x
    """
    if value < 0:
        raise ValueError("Must be a positive value")
        self.__x = value

# y
@property
def y(self):
    """
    A getter for y
    """
    return self.__y

@y.setter
def y(self, value):
    """
    A setter for y
    """
    if value < 0:
        raise ValueError("Must be a positive value")
        self.__y = value