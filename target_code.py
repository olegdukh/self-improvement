from typing import Union

def calculate(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """
    Calculates the sum of two numbers.

    This function takes two numeric arguments and returns their sum.
    It supports addition of integers and floats.

    Args:
        x: The first number, expected to be an integer or a float.
        y: The second number, expected to be an integer or a float.

    Returns:
        The sum of x and y. The return type will be float if either x or y is a float,
        otherwise it will be an int.

    Raises:
        TypeError: If the types of x and y are incompatible for addition (e.g., adding a string to a number).
                   The function relies on Python's built-in addition operator for type checking.
    """
    return x + y