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
                # Get the code, or the original sequence
                code = dictionary.get(current_sequence, current_sequence)
                
                # Convert code to bytes, with variable length
                code_bytes = code.to_bytes((code.bit_length() + 7) // 8, byteorder='big')
                compressed.extend(code_bytes)
            
            # Add new sequence to dictionary
            if next_code < 65536:  # Limit dictionary size
                dictionary[test_sequence] = next_code
                next_code += 1
            
            # Reset current sequence
            current_sequence = bytes([byte])
    
    # Add final sequence if exists
    if current_sequence:
        code = dictionary.get(current_sequence, current_sequence)
        code_bytes = code.to_bytes((code.bit_length() + 7) // 8, byteorder='big')
        compressed.extend(code_bytes)
    
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
    current_entry = None
    index = 0
    
    # Decode sequence of variable length codes
    while index < len(compressed_data):
        # Use a variable number of bytes to reconstruct the code
        max_test_length = min(len(compressed_data) - index, 4)  # Max 4 bytes for code
        
        for code_length in range(1, max_test_length + 1):
            current_code = int.from_bytes(compressed_data[index:index+code_length], byteorder='big')
            
            # Try to find a valid dictionary entry
            if current_code in dictionary:
                # Verify if this full code works
                entry = dictionary[current_code]
                result.append(entry)
                
                # If this exists in dictionary, this is our current code
                if current_entry is not None and next_code < 65536:
                    dictionary[next_code] = current_entry + entry[:1]
                    next_code += 1
                
                current_entry = entry
                index += code_length
                break
        else:
            # If no valid code found, we've hit a problem
            raise ValueError("Invalid compressed data")
    
    return b''.join(result)