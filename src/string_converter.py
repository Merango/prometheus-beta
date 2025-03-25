def to_alternating_path_case(input_string):
    """
    Convert a string to alternating path case.
    
    Alternating path case means capitalizing every other component 
    when the string is split by separators (space, underscore, or hyphen).
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to alternating path case.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> to_alternating_path_case("hello world")
        'Hello-world'
        >>> to_alternating_path_case("python_is_awesome")
        'Python-is-Awesome'
        >>> to_alternating_path_case("snake-case-example")
        'Snake-case-Example'
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty string
    if not input_string:
        return ""
    
    # Split the string by common separators
    separators = [' ', '_', '-']
    for sep in separators:
        if sep in input_string:
            # Split and capitalize every other word
            words = input_string.split(sep)
            capitalized = [word.capitalize() for i, word in enumerate(words)]
            
            # Use hyphen as the path case separator
            return '-'.join(capitalized)
    
    # If no separators found, capitalize the first letter
    return input_string.capitalize()