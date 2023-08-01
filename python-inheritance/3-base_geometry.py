#!/usr/bin/python3
"""
    This is a base class
"""


class BaseGeometry:
    """
    This is a base class
    """
    pass

# Get the list of attributes and methods using dir()
all_members = dir(BaseGeometry)

# Methods to exclude from the list
methods_to_exclude = ["__init_subclass__"]

# Filter the list to exclude the specified methods
filtered_members = [member for member in all_members if member not in methods_to_exclude]