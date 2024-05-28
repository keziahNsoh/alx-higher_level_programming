#!/usr/bin/python3
"""
This module provides a function to retrieve the list of available attributes and methods of an object.
"""

def lookup(obj):
    """
    Returns a list of attributes and methods of the given object.

    Args:
        obj: An object whose attributes and methods are to be retrieved.

    Returns:
        A list containing the names of attributes and methods of the object.
    """
    return dir(obj)

