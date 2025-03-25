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
    
    # Replace multiple separators with a single hyphen and normalize case
    import re
    
    # Normalize the string by replacing separators with hyphen and converting to lower
    normalized = re.sub(r'[ _-]+', '-', input_string.lower())
    
    # Split by hyphen
    words = normalized.split('-')
    
    # Capitalize specific words based on alternating pattern
    result_words = []
    for i, word in enumerate(words):
        if i % 2 == 0:
            # First word and every other word (even indices)
            result_words.append(word.capitalize())
        else:
            # Alternate words
            result_words.append(word)
    
    # Join with hyphen
    return '-'.join(result_words)