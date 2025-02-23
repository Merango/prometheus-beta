"""
LZH Compression Algorithm Implementation

This module provides a basic implementation of the LZH compression algorithm.
"""

def lzh_compress(data):
    """
    Compress data using the LZW compression algorithm.
    
    Args:
        data (bytes or str): Input data to compress.
    
    Returns:
        bytes: Compressed data.
    
    Raises:
        TypeError: If input is not bytes or str.
        ValueError: If input is empty.
    """
    # Validate and convert input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")
    
    # Initialize dictionary with single-byte sequences
    dictionary = {bytes([i]): i for i in range(256)}
    next_code = 256
    
    # Compression variables
    result = []
    current_sequence = bytes()
    
    # Process each byte
    for byte in data:
        # Extend current sequence
        test_sequence = current_sequence + bytes([byte])
        
        # If test sequence exists in dictionary, use it
        if test_sequence in dictionary:
            current_sequence = test_sequence
        else:
            # Output code for current sequence
            result.append(dictionary[current_sequence])
            
            # Add new sequence to dictionary if space available
            if next_code < 65536:  # Prevent dictionary overflow
                dictionary[test_sequence] = next_code
                next_code += 1
            
            # Reset current sequence to current byte
            current_sequence = bytes([byte])
    
    # Output last sequence
    if current_sequence:
        result.append(dictionary[current_sequence])
    
    # Convert to compressed format
    compressed = bytes(result)
    return compressed

def lzh_decompress(compressed_data):
    """
    Decompress data compressed with the LZH algorithm.
    
    Args:
        compressed_data (bytes): Compressed input data.
    
    Returns:
        bytes: Decompressed data.
    
    Raises:
        TypeError: If input is not bytes.
        ValueError: If input is empty or invalid.
    """
    # Validate input
    if not compressed_data:
        raise ValueError("Compressed data cannot be empty")
    
    if not isinstance(compressed_data, bytes):
        raise TypeError("Compressed data must be bytes")
    
    # Initialize dictionary with single-byte sequences
    dictionary = {i: bytes([i]) for i in range(256)}
    next_code = 256
    
    # Decompression variables
    result = []
    previous_code = compressed_data[0]
    result.extend(dictionary[previous_code])
    
    # Process remaining compressed codes
    for code in compressed_data[1:]:
        # Handle unknown code case
        if code in dictionary:
            current_sequence = dictionary[code]
        elif code == next_code:
            # Special case: sequence not yet in dictionary
            prev_sequence = dictionary[previous_code]
            current_sequence = prev_sequence + bytes([prev_sequence[0]])
        else:
            raise ValueError(f"Invalid compressed data: unknown code {code}")
        
        # Add current sequence to result
        result.extend(current_sequence)
        
        # Update dictionary if space available
        if next_code < 65536:
            prev_sequence = dictionary[previous_code]
            new_sequence = prev_sequence + bytes([current_sequence[0]])
            dictionary[next_code] = new_sequence
            next_code += 1
        
        # Update previous code
        previous_code = code
    
    return bytes(result)