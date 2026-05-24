from typing import Union

def calculate(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """
    Calculates the sum of two numbers.

    This function takes two numerical inputs and returns their sum.
    It performs type validation to ensure that both inputs are valid
    integers or floating-point numbers before performing the addition.

    Args:
        x: The first number (integer or float) to be added.
        y: The second number (integer or float) to be added.

    Returns:
        The sum of x and y (integer or float).

    Raises:
        TypeError: If either x or y is not an integer or a float.
    """
    if not isinstance(x, (int, float)):
        raise TypeError(f"Invalid type for 'x'. Expected int or float, but got {type(x).__name__}.")
    if not isinstance(y, (int, float)):
        raise TypeError(f"Invalid type for 'y'. Expected int or float, but got {type(y).__name__}.")

    return x + y