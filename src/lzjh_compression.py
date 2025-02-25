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
        # Extend current sequence
        test_sequence = current_sequence + bytes([byte])
        
        # If we've seen this sequence before, continue
        if test_sequence in dictionary:
            current_sequence = test_sequence
        else:
            # Add the code or byte for the current sequence
            if current_sequence:
                # If single byte, return the byte
                if len(current_sequence) == 1:
                    compressed.append(current_sequence[0])
                else:
                    # If multi-byte sequence, return its dictionary code
                    compressed.append(dictionary.get(current_sequence, current_sequence))
            
            # Add new sequence to dictionary
            if next_code < 65536:  # Limit dictionary size
                dictionary[test_sequence] = next_code
                next_code += 1
            
            # Reset current sequence
            current_sequence = bytes([byte])
    
    # Add final sequence if exists
    if current_sequence:
        # If single byte, return the byte
        if len(current_sequence) == 1:
            compressed.append(current_sequence[0])
        else:
            # If multi-byte sequence, return its dictionary code
            compressed.append(dictionary.get(current_sequence, current_sequence))
    
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
    
    # Initialize decompression dictionary and variables
    dictionary = {i: bytes([i]) for i in range(256)}
    next_code = 256
    result = []
    
    # First entry
    if len(compressed_data) == 0:
        return b''
    
    previous = dictionary[compressed_data[0]]
    result.append(previous)
    
    # Decompress the rest
    for code in compressed_data[1:]:
        # Determine the current entry
        if code < 256:
            # Direct byte
            entry = bytes([code])
        elif code in dictionary:
            # From dictionary
            entry = dictionary[code]
        else:
            # Predicted sequence
            entry = previous + previous[:1]
        
        # Add to result
        result.append(entry)
        
        # Add new sequence to dictionary
        if next_code < 65536:
            dictionary[next_code] = previous + entry[:1]
            next_code += 1
        
        # Update previous
        previous = entry
    
    return b''.join(result)