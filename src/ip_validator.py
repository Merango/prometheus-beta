def validate_ipv4_address(ip_address: str) -> bool:
    """
    Validate if a given string is a valid IPv4 address in the format 'A.B.C.D',
    where A, B, C, and D are single digit numeric characters between 0 and 9.

    Args:
        ip_address (str): The IP address string to validate

    Returns:
        bool: True if the IP address is valid, False otherwise
    """
    # Check if the input is a string and not empty
    if not isinstance(ip_address, str) or not ip_address:
        return False
    
    # Split the IP address into octets
    octets = ip_address.split('.')
    
    # Check if there are exactly 4 octets
    if len(octets) != 4:
        return False
    
    # Validate each octet
    for octet in octets:
        # Check if octet is exactly 1 character long
        if len(octet) != 1:
            return False
        
        # Check if octet is a digit between 0 and 9
        if not octet.isdigit() or int(octet) < 0 or int(octet) > 9:
            return False
    
    return True