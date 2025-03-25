def to_dot_case(input_string):
    """
    Convert a string to dot case.
    
    Dot case converts a string to lowercase with dots separating words.
    Handles various input formats including camelCase, snake_case, 
    PascalCase, and strings with mixed or special characters.
    
    Args:
        input_string (str): The input string to convert to dot case.
    
    Returns:
        str: The input string converted to dot case.
    
    Raises:
        TypeError: If input is not a string.
    
    Examples:
        >>> to_dot_case("HelloWorld")
        'hello.world'
        >>> to_dot_case("hello_world")
        'hello.world'
        >>> to_dot_case("Hello World")
        'hello.world'
        >>> to_dot_case("hello-world")
        'hello.world'
    """
    # Check input type
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string
    if not input_string:
        return ""
    
    # Replace non-alphanumeric characters with a single space
    import re
    # Normalize string: replace non-alphanumeric chars with space, preserve case
    normalized = re.sub(r'[^a-zA-Z0-9]+', ' ', input_string)
    
    # Split the string into words, handling camelCase and PascalCase
    words = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?=[A-Z][a-z]|\d|\W|$)|\d+', normalized)
    
    # Convert to lowercase and join with dots
    return '.'.join(word.lower() for word in words)