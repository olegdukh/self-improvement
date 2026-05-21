from typing import Union

def calculate(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """
    Calculates the sum of two numbers.

    This function adds two numeric values (integers or floats) and returns their sum.
    It includes type hinting for improved readability and maintainability, and handles
    potential TypeErrors by raising a more descriptive ValueError if the inputs
    are not compatible for addition.

    Args:
        x: The first number (integer or float) to be added.
        y: The second number (integer or float) to be added.

    Returns:
        The sum of x and y (integer or float). The type will be float if either x or y
        is a float, otherwise it will be an integer if both are integers.

    Raises:
        ValueError: If the inputs x or y are not numeric types that can be summed
                    (e.g., attempting to add a number and a string).
    """
    try:
        result = x + y
        return result
    except TypeError as e:
        # Catch TypeError if inputs are not compatible for addition (e.g., int + str)
        raise ValueError(f"Inputs 'x' and 'y' must be numeric (int or float) and summable. "
                         f"Received types: {type(x).__name__} and {type(y).__name__}.") from e