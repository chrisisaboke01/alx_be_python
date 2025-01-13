def safe_divide(numerator, denominator):
    """
    Perform division with error handling for:
    - Division by zero
    - Non-numeric inputs

    Args:
        numerator (str): The numerator as a string (will be converted to float).
        denominator (str): The denominator as a string (will be converted to float).

    Returns:
        str: The result of the division or an error message.
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        den = float(denominator)
        # Attempt the division
        result = num / den
        return f"The result of the division is {result:.2f}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
