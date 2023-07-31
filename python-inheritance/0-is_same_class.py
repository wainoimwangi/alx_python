#!/usr/bin/python3

"""
Write a function that returns True if the object is exactly
an instance of the specified class ; otherwise False.

Prototype: def is_same_class(obj, a_class):
You are not allowed to import any module
"""


def is_same_class(obj, a_class)
    """
    The is_same_class function returns True if the object obj 
    is an instance of the specified class a_class, and False 
    otherwise.
    """
    return issubclass(type(obj))
