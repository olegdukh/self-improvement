import numbers

def calculate(x: numbers.Number, y: numbers.Number) -> numbers.Number:
    """
    Calculates the sum of two numbers.

    This function takes two numerical inputs and returns their sum.
    It performs type validation to ensure that both inputs are indeed
    numerical types before attempting the addition.

    Args:
        x: The first number (e.g., int, float, complex, or other numeric type).
        y: The second number (e.g., int, float, complex, or other numeric type).

    Returns:
        The sum of x and y.

    Raises:
        TypeError: If either x or y is not an instance of a numeric type.
    """
    if not isinstance(x, numbers.Number) or not isinstance(y, numbers.Number):
        raise TypeError(
            f"Both arguments 'x' and 'y' must be numbers. "
            f"Received types: x={type(x).__name__}, y={type(y).__name__}"
        )

    return x + y