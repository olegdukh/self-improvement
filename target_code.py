def calculate(x: (int | float), y: (int | float)) -> (int | float):
    """
    Calculates the sum of two numbers.

    This function takes two numeric arguments, `x` and `y`, and returns their sum.
    It performs type validation to ensure that both inputs are valid numbers
    (integers or floats) before attempting the addition.

    Args:
        x: The first number (integer or float) to be added.
        y: The second number (integer or float) to be added.

    Returns:
        The sum of x and y (integer or float).

    Raises:
        TypeError: If either x or y is not an int or float.
    """
    if not isinstance(x, (int, float)):
        raise TypeError(f"Argument 'x' must be an int or float, but received {type(x).__name__}")
    if not isinstance(y, (int, float)):
        raise TypeError(f"Argument 'y' must be an int or float, but received {type(y).__name__}")

    # For a simple addition, the algorithm is inherently optimized.
    # The focus here is on robustness and clarity.
    return x + y