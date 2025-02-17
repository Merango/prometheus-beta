def count_set_bits(n: int) -> int:
    """
    Count the number of set bits (1s) in the binary representation of an integer.
    
    Args:
        n (int): The input integer to count set bits for.
    
    Returns:
        int: The number of set bits in the input integer.
    
    Raises:
        TypeError: If the input is not an integer.
    """
    # Check if input is an integer
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Handle negative numbers by converting to its binary representation
    if n < 0:
        n = (1 << n.bit_length()) + n
    
    # Initialize bit count
    count = 0
    
    # Count set bits using bit manipulation
    while n:
        count += n & 1  # Check least significant bit
        n >>= 1  # Right shift to check next bit
    
    return count