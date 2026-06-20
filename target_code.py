from typing import Union

def calculate(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """
    Calculates the sum of two numbers.

    This function takes two numeric arguments and returns their sum. It is designed
    to handle integers and floating-point numbers, and Python's built-in addition
    operator handles type promotion (e.g., int + float results in float).

    Args:
        x (Union[int, float]): The first number.
        y (Union[int, float]): The second number.

    Returns:
        Union[int, float]: The sum of x and y. The return type will reflect the
                           most general type of the inputs (e.g., if one input is
                           a float, the result will be a float).

    Raises:
        TypeError: If x or y are not compatible with numeric addition (e.g.,
                   attempting to add a number to a non-numeric type like a list).
    """
    return x + y