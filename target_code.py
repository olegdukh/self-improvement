import numbers
from typing import Union

def calculate(x: numbers.Number, y: numbers.Number) -> numbers.Number:
    """
    Calculates the sum of two numbers.

    This function takes two numerical inputs and returns their sum.
    It ensures that the inputs are valid numbers before performing the addition,
    providing robust error handling for non-numeric types.

    Args:
        x: The first number. Can be an integer, float, or complex number.
        y: The second number. Can be an integer, float, or complex number.

    Returns:
        The sum of x and y. The return type will follow Python's standard
        numerical promotion rules (e.g., int + float -> float,
        float + complex -> complex).

    Raises:
        TypeError: If either x or y is not a number (i.e., not an instance
                   of int, float, or complex).
    """
    # Validate inputs to ensure they are numerical types.
    # This handles potential TypeErrors proactively and provides a clearer error message.
    if not isinstance(x, numbers.Number) or not isinstance(y, numbers.Number):
        raise TypeError("Both inputs must be numbers (e.g., int, float, or complex).")
    
    # The core addition logic is straightforward and inherently optimized by Python.
    return x + y