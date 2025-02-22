def is_valid_ip_address(ip_string):
    """
    Check if a given string is a valid IPv4 address.
    
    Args:
        ip_string (str): The string to validate as an IP address
    
    Returns:
        bool: True if the string is a valid IP address, False otherwise
    """
    # Check if the input is a string
    if not isinstance(ip_string, str):
        return False
    
    # Trim whitespace
    ip_string = ip_string.strip()
    
    # Split the string into octets
    octets = ip_string.split('.')
    
    # Check if there are exactly 4 octets
    if len(octets) != 4:
        return False
    
    # Validate each octet
    for octet in octets:
        # Check if octet is a valid integer between 0 and 255
        try:
            octet_value = int(octet)
            
            # Check for leading zeros (which are not allowed)
            if len(octet) > 1 and octet[0] == '0':
                return False
            
            # Check value range
            if octet_value < 0 or octet_value > 255:
                return False
        except ValueError:
            # Non-integer or invalid numeric string
            return False
    
    return True