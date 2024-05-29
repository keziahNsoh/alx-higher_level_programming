def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first integer.
        b (int or float, optional): The second integer. Defaults to 98.

    Raises:
        TypeError: If a is not an integer or b is not an integer.

    Returns:
        int: The addition of a and b.
    """

    # Check if a and b are integers or floats
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    # Cast a and b to integers if they are floats
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    # Return the addition of a and b
    return a + b
