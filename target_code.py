from typing import Union

def calculate(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """
    Calculates the sum of two numbers.

    This function takes two numeric inputs and returns their sum.
    It includes type validation to ensure both inputs are either integers or floats.

    Args:
        x: The first number (integer or float).
        y: The second number (integer or float).

    Returns:
        The sum of x and y (integer or float).

    Raises:
        TypeError: If either x or y is not an integer or a float.
    """
    if not isinstance(x, (int, float)):
        raise TypeError(f"Input 'x' must be a numeric type (int or float), but got {type(x).__name__}")
    if not isinstance(y, (int, float)):
        raise TypeError(f"Input 'y' must be a numeric type (int or float), but got {type(y).__name__}")

    return x + y