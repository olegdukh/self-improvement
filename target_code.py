from typing import Union

def calculate(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """
    Calculates the sum of two numbers.

    This function takes two numeric arguments (integers or floats) and returns
    their sum. It performs input validation to ensure that both arguments
    are of appropriate numeric types, raising a TypeError if not.

    Args:
        x (Union[int, float]): The first number.
        y (Union[int, float]): The second number.

    Returns:
        Union[int, float]: The sum of x and y. The return type will be float
                           if either x or y is a float, otherwise int.

    Raises:
        TypeError: If either x or y is not an integer or a float.
    """
    if not isinstance(x, (int, float)):
        raise TypeError(f"Argument 'x' must be an integer or a float, but received type {type(x).__name__}.")
    if not isinstance(y, (int, float)):
        raise TypeError(f"Argument 'y' must be an integer or a float, but received type {type(y).__name__}.")

    # The '+' operator handles addition for various numeric types (int, float)
    # and performs type promotion as needed (e.g., int + float results in float).
    return x + y