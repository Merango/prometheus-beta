def to_alternating_camel_case(string: str) -> str:
    """
    Convert a given string to alternating camel case.
    
    Alternating camel case means that characters alternate between 
    uppercase and lowercase, starting with uppercase within each word.
    Preserves existing mixed case and non-letter characters.
    
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
    for word in string.split(' '):
        converted_word = []
        for i, char in enumerate(word):
            # If the character is already uppercase or lowercase, preserve its original case
            if char.isupper():
                converted_word.append(char)
            elif char.islower():
                converted_word.append(char.upper() if i % 2 == 0 else char.lower())
            else:
                # Non-alphabetic characters remain unchanged
                converted_word.append(char)
        result.append(''.join(converted_word))
    
    return ' '.join(result)