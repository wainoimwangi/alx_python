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
        if not isinstance(value, int):
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
        if not isinstance(value, int):
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
        if not isinstance(value, int):
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
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates the area of the ractangle
        """
        return self.width * self.height

    def display(self):
        """
        prints in stdout the Rectangle instance with the character '#' 
        """
        for i in range(self.y):
            print()
        for j in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """
        update the attributes of a Rectangle instance using a variable
        number of arguments passed in the *args parameter.
        """
        arguments = len(args)
        if arguments >= 1:
            self.id = args[0]
        if arguments >= 2:
            self.width = args[1]
        if arguments >= 3:
            self.height = args[2]
        if arguments >= 4:
            self.x = args[3]
        if arguments >= 5:
            self.y = args[4]

        if arguments == 0 or not kwargs:
            return
        
        for key, value in kwargs.items():
            if key == 'id':
                self.id = value
            elif key == 'width':
                self.width = value
            elif key == 'height':
                self.height = value
            elif key == 'x':
                self.x = value
            elif key == 'y':
                self.y = value

    def __str__(self):
        """
        Updates the class Rectangle by overriding the __str__ method 
        so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"