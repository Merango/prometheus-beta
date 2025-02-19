def convert_to_sponge_case(text: str) -> str:
    """
    Convert a string to sponge case, where characters alternate between 
    lowercase and uppercase.
    
    Args:
        text (str): The input string to convert
    
    Returns:
        str: The input string converted to sponge case
    
    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    return ''.join(
        char.lower() if idx % 2 == 0 else char.upper() 
        for idx, char in enumerate(text)
    )