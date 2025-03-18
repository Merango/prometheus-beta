def reverse_bits(n: int) -> int:
    """
    Reverse the bits of a given 32-bit unsigned integer.
    
    Args:
        n (int): A 32-bit unsigned integer to have its bits reversed.
    
    Returns:
        int: The integer with its bits reversed.
    
    Raises:
        ValueError: If the input is not a non-negative 32-bit integer.
    
    Examples:
        >>> reverse_bits(43261596)  # 00000010100101000001111010011100 -> 00111001011110000010100101000000
        964176192
        >>> reverse_bits(0)
        0
        >>> reverse_bits(2**32 - 1)
        4294967295
    """
    # Validate input
    if not isinstance(n, int) or n < 0 or n >= 2**32:
        raise ValueError("Input must be a 32-bit unsigned integer (0 to 2^32 - 1)")
    
    # Reverse bits using bit manipulation
    reversed_num = 0
    for i in range(32):
        # Shift the current reversed number left and add the least significant bit of n
        reversed_num = (reversed_num << 1) | (n & 1)
        # Shift n right to process next bit
        n >>= 1
    
    return reversed_num