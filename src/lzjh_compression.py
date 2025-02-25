"""
LZJH (Lempel-Ziv-Johnson-Handschin) Compression Algorithm Implementation

This module provides functions for LZJH compression and decompression.
"""

def lzjh_compress(data):
    """
    Compress input data using the LZJH compression algorithm.
    
    Args:
        data (bytes or str): Input data to be compressed
    
    Returns:
        bytes: Compressed data
    
    Raises:
        TypeError: If input is not bytes or str
        ValueError: If input is empty
    """
    # Validate input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Convert to bytes if input is string
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")
    
    # Initialize compression dictionary and variables
    dictionary = {bytes([i]): i for i in range(256)}
    next_code = 256
    current_sequence = b''
    compressed = bytearray()
    
    # Iterate through input data
    for byte in data:
        # Extend current sequence
        test_sequence = current_sequence + bytes([byte])
        
        # If we've seen this sequence before, continue
        if test_sequence in dictionary:
            current_sequence = test_sequence
        else:
            # Add the code for the current sequence
            if current_sequence:
                code = dictionary[current_sequence]
                compressed.extend(code.to_bytes((code.bit_length() + 7) // 8, byteorder='big'))
            
            # Add new sequence to dictionary
            if next_code < 65536:  # Limit dictionary size
                dictionary[test_sequence] = next_code
                next_code += 1
            
            # Reset current sequence
            current_sequence = bytes([byte])
    
    # Add final sequence if exists
    if current_sequence:
        code = dictionary[current_sequence]
        compressed.extend(code.to_bytes((code.bit_length() + 7) // 8, byteorder='big'))
    
    return bytes(compressed)

def lzjh_decompress(compressed_data):
    """
    Decompress data compressed with the LZJH algorithm.
    
    Args:
        compressed_data (bytes): Compressed input data
    
    Returns:
        bytes: Decompressed data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If input is empty
    """
    # Validate input
    if not compressed_data:
        raise ValueError("Compressed data cannot be empty")
    
    if not isinstance(compressed_data, bytes):
        raise TypeError("Compressed data must be bytes")
    
    # Initialize decompression dictionary
    dictionary = {i: bytes([i]) for i in range(256)}
    next_code = 256
    result = []
    
    # Helper function to read next code
    def read_next_code(data_slice):
        code = 0
        consumed_bytes = 0
        while data_slice:
            code = (code << 8) | data_slice[0]
            data_slice = data_slice[1:]
            consumed_bytes += 1
            
            # Try looking up the code
            if code in dictionary:
                return code, consumed_bytes, data_slice
        
        raise ValueError("Invalid compressed data")
    
    # Initial entry
    current_code, bytes_used, remaining = read_next_code(compressed_data)
    current = dictionary[current_code]
    result.append(current)
    
    # Decompress the rest
    while remaining:
        # Get next code
        next_code_val, used, remaining = read_next_code(remaining)
        
        # Determine the current entry
        if next_code_val in dictionary:
            entry = dictionary[next_code_val]
        elif next_code_val == next_code:
            # Special case: new sequence predicted
            entry = current + current[:1]
        else:
            raise ValueError(f"Invalid compressed code: {next_code_val}")
        
        # Add to result
        result.append(entry)
        
        # Add new sequence to dictionary
        if next_code < 65536:
            dictionary[next_code] = current + entry[:1]
            next_code += 1
        
        # Update current
        current = entry
    
    return b''.join(result)