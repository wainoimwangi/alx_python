#!/usr/bin/python3
"""
    This is a base class
"""


class BaseGeometry:
    """
    This is a base class
    """
    pass

class MyNewClass:
    def __dir__(cls) -> None:
        attributes = super().__dir__()

        return [attribute for attribute in attributes if attribute != '__init_subclass__']
