def convert_to_header_case(text: str) -> str:
    """
    Convert a string to header case (capitalized first letter of each word).
    
    Args:
        text (str): Input string to convert
    
    Returns:
        str: String converted to header case
    
    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    # Split by various delimiters: spaces, underscores, hyphens
    words = text.replace('_', ' ').replace('-', ' ').split()
    
    # Capitalize first letter of each word, handle empty input
    return ' '.join(word.capitalize() for word in words) if words else ''