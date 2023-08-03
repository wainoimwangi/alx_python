#!/usr/bin/python3
"""
    This is a base class
"""


class BaseGeometry:
    """
    This is a base class
    """
    pass

class MyNewClass(BaseGeometry):
    def __dir__(cls) -> None:
        """
        Exclude attribute init subclass in dir()
        """
        attributes = super().__dir__()

        return [attribute for attribute in attributes if attribute != '__init_subclass__']
