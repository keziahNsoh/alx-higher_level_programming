#!/usr/bin/python3
"""
This module provides a class MyList that inherits from list.
"""

class MyList(list):
    """
    A class that inherits from list and provides additional functionality.
    """

    def print_sorted(self):
        """
        Prints the list in sorted order (ascending).

        Args:
            None

        Returns:
            None
        """
        sorted_list = sorted(self)
        print(sorted_list)

if __name__ == "__main__":
    my_list = MyList([3, 1, 4, 2])
    my_list.print_sorted()

