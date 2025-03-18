def to_alternating_camel_case(string: str) -> str:
    """
    Convert a given string to alternating camel case.
    
    Alternating camel case means that characters alternate between 
    uppercase and lowercase, starting with uppercase.
    
    Args:
        string (str): The input string to convert
    
    Returns:
        str: The string converted to alternating camel case
    
    Raises:
        TypeError: If input is not a string
        ValueError: If input string is empty
    
    Examples:
        >>> to_alternating_camel_case("hello world")
        'HeLlO WoRlD'
        >>> to_alternating_camel_case("python programming")
        'PyThOn PrOgRaMmInG'
    """
    # Check input type
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
    
    # Check for empty string
    if not string:
        raise ValueError("Input string cannot be empty")
    
    # Convert to alternating case
    result = []
    should_upper = True
    for char in string:
        if char.isalpha():
            # For alphabetic characters, alternate case
            result.append(char.upper() if should_upper else char.lower())
            should_upper = not should_upper
        else:
            # For non-alphabetic characters, keep as-is
            result.append(char)
    
    return ''.join(result)