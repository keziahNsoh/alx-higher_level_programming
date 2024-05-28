#!/usr/bin/python3
"""
This module provides a class BaseGeometry.
"""

class BaseGeometry:
    """
    A class representing basic geometry.
    """

    def area(self):
        """
        Computes the area of the geometry.

        Raises:
            Exception: Always raises an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

