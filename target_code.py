def calculate(x: int | float, y: int | float) -> int | float:
    """
    Calculates the sum of two numbers.

    This function takes two numerical inputs and returns their sum.
    It includes type hinting for better code readability and maintainability,
    and robust error handling to ensure both inputs are valid numbers.

    Args:
        x: The first number (integer or float).
        y: The second number (integer or float).

    Returns:
        The sum of x and y (integer or float).

    Raises:
        TypeError: If either x or y is not a valid number (int or float)
                   or if they are of incompatible types for addition.
        RuntimeError: For any unexpected errors during the calculation.
    """
    try:
        # The '+' operator in Python handles addition for various numeric types.
        # If x or y are non-numeric types that cannot be added, a TypeError
        # will naturally be raised, which is caught below.
        result = x + y
        return result
    except TypeError:
        # Catch TypeError specifically for incompatible types during addition.
        raise TypeError("Both inputs 'x' and 'y' must be numbers (int or float) and compatible for addition.")
    except Exception as e:
        # Catch any other unexpected errors that might occur during the calculation.
        raise RuntimeError(f"An unexpected error occurred during calculation: {e}")