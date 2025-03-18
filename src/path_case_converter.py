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
    
    # Insert slash between lower-uppercase transitions 
    # (Handling camel case by splitting words)
    path_case = re.sub(r'(?<!^)(?=[A-Z])', '/', input_string)
    
    # Convert to lowercase
    path_case = path_case.lower()
    
    # Replace any non-alphanumeric characters with forward slash
    path_case = re.sub(r'[^a-z0-9]+', '/', path_case)
    
    # Remove multiple consecutive slashes
    path_case = re.sub(r'/+', '/', path_case)
    
    # Remove leading/trailing slashes
    path_case = path_case.strip('/')
    
    return path_case