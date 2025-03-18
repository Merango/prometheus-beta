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
    for i, char in enumerate(string):
        # Even indices (0, 2, 4...) are uppercase
        # Odd indices (1, 3, 5...) are lowercase
        if i % 2 == 0:
            result.append(char.upper())
        else:
            result.append(char.lower())
    
    return ''.join(result)