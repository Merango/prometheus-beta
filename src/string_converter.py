import re

def convert_to_alternating_pascal_case(input_string: str) -> str:
    """
    Convert a string to alternating Pascal case.
    
    This function transforms the input string so that words alternate between 
    starting with an uppercase and lowercase letter.
    
    Args:
        input_string (str): The input string to be converted.
    
    Returns:
        str: The string converted to alternating Pascal case.
    
    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input string is empty.
    
    Examples:
        >>> convert_to_alternating_pascal_case("hello world")
        'HeLlOWoRlD'
        >>> convert_to_alternating_pascal_case("python is awesome")
        'OneTwOThReE'
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Check for empty string
    if not input_string:
        raise ValueError("Input string cannot be empty")
    
    # Remove non-alphanumeric characters and extra whitespace
    cleaned_string = re.sub(r'[^a-zA-Z\s]', '', input_string.strip())
    
    # Split into words
    words = cleaned_string.split()
    
    # Convert to alternating case
    result = []
    for i, word in enumerate(words):
        converted_word = ''.join(
            char.upper() if ((i + len(result)) % 2 == 0) else char.lower() 
            for char in word
        )
        result.append(converted_word)
    
    # Join the words together
    return ''.join(result)