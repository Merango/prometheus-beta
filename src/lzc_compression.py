"""
LZC (Lempel-Ziv-Cheung) Compression Algorithm Implementation.

This module provides functions for LZC compression, which is a variant 
of the Lempel-Ziv compression algorithm.
"""

def lzc_compress(input_data):
    """
    Compress input data using the LZC (Lempel-Ziv-Cheung) algorithm.

    Args:
        input_data (str or bytes): The data to be compressed.

    Returns:
        list: A list of integers representing the compressed data.

    Raises:
        TypeError: If input is not a string or bytes.
        ValueError: If input is empty.
    """
    # Input validation
    if not input_data:
        raise ValueError("Input data cannot be empty")
    
    # Convert to bytes if input is a string
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')
    elif not isinstance(input_data, bytes):
        raise TypeError("Input must be a string or bytes")

    # Initialize dictionary with single-byte entries
    dictionary = {bytes([i]): i for i in range(256)}
    next_code = 256
    
    # Compression variables
    compressed = []
    current_sequence = bytes()

    # Compression algorithm
    for byte in input_data:
        # Extend current sequence
        test_sequence = current_sequence + bytes([byte])
        
        # If sequence is in dictionary, continue building
        if test_sequence in dictionary:
            current_sequence = test_sequence
        else:
            # Output the code for current sequence
            compressed.append(dictionary[current_sequence])
            
            # Add new sequence to dictionary if not at max size
            if next_code < 65536:  # Limit dictionary size
                dictionary[test_sequence] = next_code
                next_code += 1
            
            # Reset current sequence to last byte
            current_sequence = bytes([byte])
    
    # Add last sequence code
    if current_sequence:
        compressed.append(dictionary[current_sequence])
    
    return compressed

def lzc_decompress(compressed_data):
    """
    Decompress data that was compressed using the LZC algorithm.

    Args:
        compressed_data (list): A list of integers representing compressed data.

    Returns:
        bytes: The decompressed data.

    Raises:
        TypeError: If input is not a list of integers.
        ValueError: If input is empty or contains invalid codes.
    """
    # Input validation
    if not isinstance(compressed_data, list):
        raise TypeError("Input must be a list of integers")
    
    if not compressed_data:
        raise ValueError("Compressed data cannot be empty")
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in compressed_data):
        raise TypeError("All elements must be integers")

    # Initialize dictionary with single-byte entries
    dictionary = {i: bytes([i]) for i in range(256)}
    next_code = 256
    
    # Decompression variables
    decompressed = []
    previous_code = compressed_data[0]
    result = dictionary[previous_code]
    decompressed.extend(result)

    # Decompression algorithm
    for code in compressed_data[1:]:
        # Check if code is in dictionary
        if code in dictionary:
            entry = dictionary[code]
        elif code == next_code:
            # Special case: new sequence not yet in dictionary
            entry = dictionary[previous_code] + bytes([dictionary[previous_code][0]])
        else:
            raise ValueError(f"Invalid compression code: {code}")
        
        # Extend decompressed result
        decompressed.extend(entry)
        
        # Add new sequence to dictionary if not at max size
        if next_code < 65536:
            # New sequence is previous entry + first byte of current entry
            new_sequence = dictionary[previous_code] + bytes([entry[0]])
            dictionary[next_code] = new_sequence
            next_code += 1
        
        # Update previous code
        previous_code = code

    return bytes(decompressed)