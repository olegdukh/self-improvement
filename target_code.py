import numbers
from typing import Union

def calculate(x: numbers.Number, y: numbers.Number) -> Union[int, float]:
    """
    Calculates the sum of two numbers.

    This function takes two numeric inputs and returns their sum.
    It ensures that the inputs are valid numbers before performing the operation.

    Args:
        x (numbers.Number): The first number (integer, float, or other numeric type).
        y (numbers.Number): The second number (integer, float, or other numeric type).

    Returns:
        Union[int, float]: The sum of x and y. The return type will be int if both
                           inputs are integers and their sum is an integer, otherwise float.

    Raises:
        TypeError: If either x or y is not a numeric type.
    """
    if not isinstance(x, numbers.Number) or not isinstance(y, numbers.Number):
        raise TypeError("Both inputs must be numbers (e.g., int, float).")

    return x + y