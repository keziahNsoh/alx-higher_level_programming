#!/usr/bin/python3
"""
This module provides a class Rectangle that inherits from BaseGeometry.
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

    def integer_validator(self, name, value):
        """
        Validates the value.

        Args:
            name: A string representing the name of the value.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with the given width and height.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """
        Computes the area of the rectangle.

        Returns:
            The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            A string representing the rectangle in the format [Rectangle] <width>/<height>.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def __repr__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            A string representing the rectangle in the format [Rectangle] <width>/<height>.
        """
        return self.__str__()

