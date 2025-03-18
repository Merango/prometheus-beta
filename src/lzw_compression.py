"""
Lempel-Ziv-Welch (LZW) Compression Algorithm Implementation

This module provides functions for LZW compression and decompression.
"""

def lzw_compress(data):
    """
    Compress the input data using the Lempel-Ziv-Welch (LZW) algorithm.
    
    Args:
        data (str): The input string to be compressed.
    
    Returns:
        list: A list of integer codes representing the compressed data.
    
    Raises:
        TypeError: If input is not a string.
        ValueError: If input is an empty string.
    """
    # Input validation
    if not isinstance(data, str):
        raise TypeError("Input must be a string")
    
    if not data:
        raise ValueError("Input cannot be an empty string")
    
    # Initialize dictionary with single-character strings
    dictionary = {chr(i): i for i in range(256)}
    next_code = 256
    
    # Compression process
    result = []
    current_sequence = data[0]
    
    for char in data[1:]:
        # Check if current_sequence + char is in dictionary
        test_sequence = current_sequence + char
        
        if test_sequence in dictionary:
            # If exists, extend current sequence
            current_sequence = test_sequence
        else:
            # Output code for current sequence
            result.append(dictionary[current_sequence])
            
            # Add new sequence to dictionary
            dictionary[test_sequence] = next_code
            next_code += 1
            
            # Reset current sequence
            current_sequence = char
    
    # Output code for last sequence
    if current_sequence:
        result.append(dictionary[current_sequence])
    
    return result

def lzw_decompress(compressed_data):
    """
    Decompress data previously compressed using the LZW algorithm.
    
    Args:
        compressed_data (list): List of integer codes to decompress.
    
    Returns:
        str: The decompressed original string.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If input list is empty or contains invalid codes.
    """
    # Input validation
    if not isinstance(compressed_data, list):
        raise TypeError("Input must be a list of integer codes")
    
    if not compressed_data:
        raise ValueError("Input cannot be an empty list")
    
    # Initialize dictionary with single-character strings
    dictionary = {i: chr(i) for i in range(256)}
    next_code = 256
    
    # First code is always decoded directly
    result = [dictionary[compressed_data[0]]]
    current_code = compressed_data[0]
    
    for code in compressed_data[1:]:
        # Retrieve current string from dictionary
        if code in dictionary:
            current_string = dictionary[code]
        elif code == next_code:
            # Special case: code not yet in dictionary
            current_string = dictionary[current_code] + dictionary[current_code][0]
        else:
            raise ValueError(f"Invalid compression code: {code}")
        
        # Output current string
        result.append(current_string)
        
        # Add new entry to dictionary
        dictionary[next_code] = dictionary[current_code] + current_string[0]
        next_code += 1
        
        # Update current code
        current_code = code
    
    # Convert list of strings to single string
    return ''.join(result)