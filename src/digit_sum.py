def sum_of_digits(input_string):
    """
    Calculate the sum of digits in a given string.

    This function extracts all digits from the input string and returns their sum.
    Leading zeros are ignored.

    Args:
        input_string (str): The input string to extract digits from.

    Returns:
        int: The sum of all digits in the string.

    Examples:
        >>> sum_of_digits('1234567890')
        45
        >>> sum_of_digits('abc123')
        6
        >>> sum_of_digits('no digits')
        0
    """
    # Extract digits, convert to int to remove leading zeros
    digits = [int(char) for char in input_string if char.isdigit()]
    
    # Return the sum of digits (0 if no digits found)
    return sum(digits)