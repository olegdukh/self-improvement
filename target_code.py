def calculate(x: "Union[int, float]", y: "Union[int, float]") -> "Union[int, float]":
    """
    Calculates the sum of two numbers.

    This function takes two numerical inputs and returns their sum.
    It performs type checking to ensure that both inputs are valid numbers
    (integers or floats) before proceeding with the addition.

    Args:
        x: The first number, which can be an integer or a float.
        y: The second number, which can be an integer or a float.

    Returns:
        The sum of x and y, which will be an integer or a float.

    Raises:
        TypeError: If either x or y is not an integer or a float.
    """
    if not isinstance(x, (int, float)):
        raise TypeError(f"Argument 'x' must be an integer or a float, but received type {type(x).__name__}")
    if not isinstance(y, (int, float)):
        raise TypeError(f"Argument 'y' must be an integer or a float, but received type {type(y).__name__}")

    return x + y