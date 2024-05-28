#!/usr/bin/python3
"""
This module provides a function to check if an object is exactly an instance of the specified class.
"""

def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class.

    Args:
        obj: An object to be checked.
        a_class: The class to check against.

    Returns:
        True if the object is exactly an instance of the specified class, False otherwise.
    """
    return type(obj) is a_class

