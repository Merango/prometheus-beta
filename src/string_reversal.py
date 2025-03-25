def recursive_reverse(s: str) -> str:
    """
    Recursively reverse a given string.

    Args:
        s (str): The input string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If input is not a string.
    """
    # Check if input is a string
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Base cases
    if len(s) <= 1:
        return s
    
    # Recursive case: take first character and place at the end after recursively 
    # reversing the rest of the string
    return recursive_reverse(s[1:]) + s[0]