def safe_divide(numerator, denominator):
    """
    Performs division with error handling.

    Args:
        numerator (str): Numerator value
        denominator (str): Denominator value

    Returns:
        str: Result or error message
    """
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        if denominator == 0:
            raise ZeroDivisionError
        result = numerator / denominator
        return f"The result of the division is {result:.2f}"
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

