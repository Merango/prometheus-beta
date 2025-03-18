def is_digits_only(input_string: str) -> bool:
    """
    Check if the input string contains only digits.

    Args:
        input_string (str): The string to validate.

    Returns:
        bool: True if the string contains only digits, False otherwise.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Check if the string is empty
    if not input_string:
        return False
    
    # Use str.isnumeric() which handles unicode digits more precisely
    # and ensures the entire string is numeric
    return input_string.isnumeric()