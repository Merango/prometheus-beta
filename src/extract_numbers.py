import re
from typing import List

def extract_numbers(input_string: str) -> List[int]:
    """
    Extract all integers from a given string.

    Args:
        input_string (str): The input string to extract numbers from.

    Returns:
        List[int]: A list of integers found in the input string.

    Raises:
        TypeError: If input is not a string.

    Examples:
        >>> extract_numbers("I have 42 apples and 7 oranges")
        [42, 7]
        >>> extract_numbers("No numbers here")
        []
        >>> extract_numbers("Negative numbers -123 and 456")
        [-123, 456]
    """
    # Validate input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Use regex to find all integers (including negative numbers)
    # This will match optional minus sign followed by one or more digits
    numbers = re.findall(r'-?\d+', input_string)
    
    # Convert found number strings to integers
    return [int(num) for num in numbers]