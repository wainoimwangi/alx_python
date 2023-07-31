#!/usr/bin/python3



"""
Write a function that returns True if the object is exactly
an instance of the specified class ; otherwise False.

Prototype: def is_same_class(obj, a_class):
You are not allowed to import any module
"""


class a_class:
    """
    Represents a clas with an instance attribute 'a_class'.
    That checks whether an instance of an object belongs to the 
    specified same class.
        
    Parameters:
    obj : any
        The object to be checked for its class membership.
    a_class : class
        The class that the object's membership is to be tested against.

    Method
        is_same_class(obj, a_class)
    """
    def is_same_class(obj, a_class)
        """
        The is_same_class function returns True if the object obj 
        is an instance of the specified class a_class, and False 
        otherwise.
        Returns:
        True if the object is exactly an instance of the specified class; otherwise, False.

        """
        return issubclass(type(obj))
