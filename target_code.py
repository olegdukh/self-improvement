from typing import Union

def calculate(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """
    Calculates the sum of two numbers.

    This function takes two numerical inputs and returns their sum.
    It includes type validation to ensure both inputs are integers or floats.

    Args:
        x: The first number (integer or float).
        y: The second number (integer or float).

    Returns:
        The sum of x and y (integer or float).

    Raises:
        TypeError: If either x or y is not an integer or a float.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Argument 'x' must be an integer or a float.")
    if not isinstance(y, (int, float)):
        raise TypeError("Argument 'y' must be an integer or a float.")

    return x + y