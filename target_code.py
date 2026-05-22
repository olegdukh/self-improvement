from typing import Union

def calculate(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """
    Calculates the sum of two numbers.

    This function takes two numeric arguments and returns their sum.
    It includes type hinting for clarity and handles potential TypeErrors
    if non-numeric values are provided, ensuring robust operation.

    Args:
        x (Union[int, float]): The first number.
        y (Union[int, float]): The second number.

    Returns:
        Union[int, float]: The sum of x and y.

    Raises:
        TypeError: If either x or y is not a number (int or float) and thus
                   cannot be added.
        RuntimeError: For any other unexpected errors during the calculation.
    """
    try:
        # The core logic for addition remains simple and efficient.
        return x + y
    except TypeError:
        # Catch TypeError if operands are of incompatible types (e.g., string + int)
        raise TypeError("Both arguments must be numbers (int or float) for addition.")
    except Exception as e:
        # Catch any other unexpected errors that might occur
        raise RuntimeError(f"An unexpected error occurred during calculation: {e}")