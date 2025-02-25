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
    dictionary = {}
    next_code = 256
    current_sequence = b''
    compressed = []
    
    # Iterate through input data
    for byte in data:
        # Create current sequence with new byte
        current_sequence += bytes([byte])
        
        # If sequence not in dictionary, add it
        if current_sequence not in dictionary:
            # Output the code for the previous sequence
            if len(current_sequence) > 1:
                compressed.append(dictionary.get(current_sequence[:-1], current_sequence[:-1]))
            
            # Add current sequence to dictionary if it doesn't use reserved codes
            if next_code < 65536:  # Limit dictionary size
                dictionary[current_sequence] = next_code
                next_code += 1
            
            # Reset to last byte
            current_sequence = bytes([byte])
    
    # Add final sequence
    if current_sequence:
        compressed.append(dictionary.get(current_sequence, current_sequence))
    
    return b''.join(compressed)

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
    
    # Initialize decompression dictionary and variables
    dictionary = {i: bytes([i]) for i in range(256)}
    next_code = 256
    result = []
    previous = compressed_data[:1]
    result.append(previous)
    
    # Decompress the data
    for code in compressed_data[1:]:
        # Handle different scenarios for dictionary lookup
        current = dictionary.get(code, None)
        
        if current is None:
            # Special case: current code not in dictionary
            current = previous + previous[:1]
        
        result.append(current)
        
        # Add new sequence to dictionary
        if next_code < 65536:  # Limit dictionary size
            dictionary[next_code] = previous + current[:1]
            next_code += 1
        
        previous = current
    
    return b''.join(result)