#!/usr/bin/python3
"""
This module provides a class MyInt that inherits from int.
"""

class MyInt(int):
    """
    A class representing a rebel integer.
    """

    def __eq__(self, other):
        """
        Override the equality operator.

        Args:
            other: The value to compare with.

        Returns:
            True if self is not equal to other; otherwise False.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the not equal operator.

        Args:
            other: The value to compare with.

        Returns:
            True if self is equal to other; otherwise False.
        """
        return super().__eq__(other)

