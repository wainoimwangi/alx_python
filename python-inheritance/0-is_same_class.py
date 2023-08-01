#!/usr/bin/python3
"""
Check if the given object is exactly an instance of the specified class.

Parameters:
obj : any
    The object to be checked for its class membership.
a_class : class
    The class that the object's membership is to be tested against.

Returns:
bool
    True if the object is exactly an instance of the specified class; otherwise, False.

Example:
>>> class Person:
...     pass
...
>>> class Student(Person):
...     pass
...
>>> obj = Person()
>>> is_same_class(obj, Person)
True
>>> is_same_class(obj, Student)
False
"""


class sameClass:
    """
    Check if the given object is exactly an instance of the specified class.
    """
    def is_same_class(obj, a_class):
        """
        The function checks if the given object 
        is exactly an instance of the specified class.
        """
        return issubclass(type(obj))
