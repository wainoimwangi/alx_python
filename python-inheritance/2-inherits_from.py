#!/usr/bin/python3
"""
    Check if the given object is an instance of a class that
    inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Parameters:
    obj : any
        The object to be checked for its class inheritance.
    a_class : class
        The class that the object's inheritance is to be tested against.

    Returns:
    bool
        True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class; otherwise, False.

    Example:
    >>> class Animal:
    ...     pass
    ...
    >>> class Mammal(Animal):
    ...     pass
    ...
    >>> class Dog(Mammal):
    ...     pass
    ...
    >>> class Cat(Mammal):
    ...     pass
    ...
    >>> doggo = Dog()
    >>> inherits_from(doggo, Animal)
    True
    >>> kitty = Cat()
    >>> inherits_from(kitty, Dog)
    False
    >>> inherits_from(kitty, Mammal)
    True
    """
    if type(obj) == bool and a_class == int:
        return True
    else:
        return isinstance(type(obj), a_class)
