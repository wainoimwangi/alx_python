#!/usr/bin/python3
"""
    Check if the given object is an instance of, or if the object is an instance of a class
    that inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Parameters:
    obj : any
        The object to be checked for its class membership.
    a_class : class
        The class that the object's membership is to be tested against.

    Returns:
    bool
        True if the object is an instance of, or if the object is an instance of a class
        that inherited from, the specified class; otherwise, False.

    Example:
    >>> class Animal:
    ...     pass
    ...
    >>> class Dog(Animal):
    ...     pass
    ...
    >>> class Cat(Animal):
    ...     pass
    ...
    >>> doggo = Dog()
    >>> is_kind_of_class(doggo, Dog)
    True
    >>> is_kind_of_class(doggo, Animal)
    True
    >>> kitty = Cat()
    >>> is_kind_of_class(kitty, Dog)
    False
    """
    return isinstance(type(obj), a_class)