import re

def convert_to_path_case(input_string: str) -> str:
    """
    Convert a given string to path case (lowercase with forward slashes).

    Args:
        input_string (str): The input string to be converted.

    Returns:
        str: The input string converted to path case.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input string is empty.
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Check for empty string
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Remove leading/trailing whitespace
    input_string = input_string.strip()
    
    # Convert to lowercase
    input_string = input_string.lower()
    
    # Insert forward slash between words or camel case
    # This regex handles both consecutive non-alphanumeric chars and 
    # camel case by inserting a slash
    path_case = re.sub(r'[^a-z0-9]+', '/', 
                       re.sub(r'(?<!^)(?=[A-Z])', '/', input_string))
    
    # Remove leading/trailing slashes and handle multiple consecutive slashes
    path_case = re.sub(r'/+', '/', path_case).strip('/')
    
    return path_case