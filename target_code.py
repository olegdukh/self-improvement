from typing import Union

def calculate(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """
    Calculates the sum of two numbers.

    This function takes two numeric arguments (integers or floats) and returns
    their sum. It includes type hinting for clarity.

    Args:
        x: The first number (integer or float).
        y: The second number (integer or float).

    Returns:
        The sum of x and y (integer or float).

    Raises:
        TypeError: If either x or y is not a numeric type that supports
                   the addition operation, as per Python's built-in behavior.
    """
    return x + y