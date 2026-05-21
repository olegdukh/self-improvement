from typing import Union

def calculate(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """
    Calculates the sum of two numbers.

    This function takes two numerical inputs and returns their sum.
    It performs type checking to ensure that both inputs are valid
    numerical types (int or float) before performing the addition.

    Args:
        x (Union[int, float]): The first number to be added.
        y (Union[int, float]): The second number to be added.

    Returns:
        Union[int, float]: The sum of x and y. The return type will
                           be float if either x or y is a float, otherwise int.

    Raises:
        TypeError: If either x or y is not an int or a float.
    """
    if not isinstance(x, (int, float)):
        raise TypeError(f"Argument 'x' must be an int or float, but received type {type(x).__name__}.")
    if not isinstance(y, (int, float)):
        raise TypeError(f"Argument 'y' must be an int or float, but received type {type(y).__name__}.")

    return x + y