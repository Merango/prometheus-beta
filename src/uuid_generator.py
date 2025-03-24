import uuid

def generate_uuid() -> str:
    """
    Generate a new Universally Unique Identifier (UUID).
    
    Returns:
        str: A randomly generated UUID as a string in standard format.
    
    Examples:
        >>> generated_uuid = generate_uuid()
        >>> len(generated_uuid) == 36  # Standard UUID length
        True
        >>> '-' in generated_uuid
        True
    """
    return str(uuid.uuid4())