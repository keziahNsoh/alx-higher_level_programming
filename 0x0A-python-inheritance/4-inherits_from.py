#!/usr/bin/python3
"""
This module provides a function to check if an object is an instance of a class that inherited (directly or indirectly) from the specified class.
"""

def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited (directly or indirectly) from the specified class.

    Args:
        obj: An object to be checked.
        a_class: The class to check against.

    Returns:
        True if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class

