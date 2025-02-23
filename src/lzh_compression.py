"""
LZH (Lempel-Ziv-Huffman) Compression Algorithm Implementation

This module provides a basic implementation of the LZH compression algorithm.
"""

def lzh_compress(data):
    """
    Compress the input data using LZH compression algorithm.
    
    Args:
        data (bytes or str): The input data to be compressed.
    
    Returns:
        bytes: Compressed data.
    
    Raises:
        TypeError: If input is not bytes or str.
        ValueError: If input is empty.
    """
    # Validate input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Convert to bytes if input is a string
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")
    
    # Initialize compression dictionary and variables
    dictionary = {bytes([i]): i for i in range(256)}
    next_code = 256
    current_sequence = bytes()
    compressed = []
    
    # LZH compression logic
    for byte in data:
        # Extend current sequence
        current_sequence += bytes([byte])
        
        # If sequence not in dictionary, add to compressed and update dictionary
        if current_sequence not in dictionary:
            # Output the code for the previous sequence
            compressed.append(dictionary[current_sequence[:-1]])
            
            # Add new sequence to dictionary if not at max
            if next_code < 65536:  # Limit dictionary size
                dictionary[current_sequence] = next_code
                next_code += 1
            
            # Reset current sequence to last byte
            current_sequence = bytes([byte])
    
    # Add last sequence
    if current_sequence:
        compressed.append(dictionary[current_sequence])
    
    # Convert to bytes
    return bytes(compressed)

def lzh_decompress(compressed_data):
    """
    Decompress data compressed with LZH algorithm.
    
    Args:
        compressed_data (bytes): The compressed input data.
    
    Returns:
        bytes: Decompressed data.
    
    Raises:
        TypeError: If input is not bytes.
        ValueError: If input is empty.
    """
    # Validate input
    if not compressed_data:
        raise ValueError("Compressed data cannot be empty")
    
    if not isinstance(compressed_data, bytes):
        raise TypeError("Compressed data must be bytes")
    
    # Initialize decompression dictionary
    dictionary = {i: bytes([i]) for i in range(256)}
    next_code = 256
    
    # First code is always output
    result = [compressed_data[0]]
    current = dictionary[compressed_data[0]]
    
    # Decompress remaining data
    for code in compressed_data[1:]:
        # Decode current sequence
        if code in dictionary:
            sequence = dictionary[code]
        elif code == next_code:
            # Special case for new sequence
            sequence = current + bytes([current[0]])
        else:
            raise ValueError("Invalid compressed data")
        
        # Output decoded sequence
        result.extend(sequence)
        
        # Update dictionary if possible
        if next_code < 65536:
            dictionary[next_code] = current + bytes([sequence[0]])
            next_code += 1
        
        # Update current
        current = sequence
    
    return bytes(result)