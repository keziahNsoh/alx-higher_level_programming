#!/usr/bin/python3
"""
Defining a class of rectangle
"""


class Rectangle:
    """rectangle adjustifying"""

    number_of_instances = 0
    """int: the number of instances"""

    print_symbol = '#'
    """type: print symbol for the rectangle"""

    def __init__(self, width=0, height=0):
        """Intiation of the variables"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retrival of the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrival of the value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """returning the visual shape of the rectangle using #"""
        if not self.__width or not self.__height:
            return ""
        return ((str(self.print_symbol) * self.width + "\n") * self.height)[:-1]

    def __repr__(self):
        """returning a value of a string of the rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """deleting an instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """function to compare rectangles

        Args:
            rect_1: rectangle 1
            rect_2: rectangle 2
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """return an Rectangle instance with equal size"""
        return cls(size, size)
