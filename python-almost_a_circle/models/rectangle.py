#!/usr/bin/python3
"""
    Class Rectangle that inherits from Base
    Private instance attributes with gettera and setters:
        width
        height
        x
        y
    Class constructor: def_init_(self,width,height,x,y,id=None)
        Calls the super class id
        Assigns each argument to the right attribute
"""
from models.base import Base

class Rectangle(Base):
    """
    Rectangle class that contains private instance
    variables: width, height, x and y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
       """
       function that assigns variables their correct attributes
       """
       super().__init__(id)
       self.__width = None
       self.__height = None
       self.__x = None
       self.__y = None
       self.width = width
       self.height = height
       self.x = x
       self.y = y

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
        if not isinstance(self, value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if not isinstance(self, value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
        if not isinstance(self, value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
        if not isinstance(self, value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
