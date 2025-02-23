"""
LZH (Lempel-Ziv-Huffman) Compression Algorithm Implementation

This module provides a basic implementation of the LZH compression algorithm.
"""

def encode_length(length):
    """
    Encode the length as a variable-length sequence.
    
    Args:
        length (int): Length to encode.
    
    Returns:
        bytes: Encoded length.
    """
    result = []
    while length > 0:
        byte = length & 0x7F
        length >>= 7
        if length > 0:
            byte |= 0x80  # Set continuation bit
        result.insert(0, byte)
    
    return bytes(result) if result else bytes([0])

def decode_length(data):
    """
    Decode a variable-length length.
    
    Args:
        data (bytes): Sequence to decode.
    
    Returns:
        tuple: (decoded length, bytes read)
    """
    length = 0
    bytes_read = 0
    
    for byte in data:
        bytes_read += 1
        length = (length << 7) | (byte & 0x7F)
        if byte & 0x80 == 0:
            break
    
    return length, bytes_read

def lzh_compress(data):
    """
    Compress the input data using a modified LZW algorithm.
    
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
    
    # Initialize dictionary and variables
    dictionary = {bytes([i]): i for i in range(256)}
    next_code = 256
    current_sequence = bytes()
    compressed = []
    
    # Compression loop
    for byte in data:
        # Extend current sequence
        current_sequence += bytes([byte])
        
        # If current sequence not in dictionary
        if current_sequence not in dictionary:
            # Output previous sequence's code
            prev_code = dictionary[current_sequence[:-1]]
            compressed.extend(encode_length(prev_code))
            
            # Add new sequence to dictionary if space available
            if next_code < 65536:
                dictionary[current_sequence] = next_code
                next_code += 1
            
            # Reset current sequence
            current_sequence = bytes([byte])
    
    # Output last sequence
    if current_sequence:
        compressed.extend(encode_length(dictionary[current_sequence]))
    
    return bytes(compressed)

def lzh_decompress(compressed_data):
    """
    Decompress data compressed with the LZW algorithm.
    
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
    
    # Initialize dictionary
    dictionary = {i: bytes([i]) for i in range(256)}
    next_code = 256
    
    # Decompression variables
    index = 0
    result = []
    previous_code = None
    
    # Process entire compressed data
    while index < len(compressed_data):
        # Decode current code
        current_code, bytes_read = decode_length(compressed_data[index:])
        index += bytes_read
        
        # Retrieve current sequence
        if current_code in dictionary:
            current_sequence = dictionary[current_code]
        elif current_code == next_code and previous_code is not None:
            # Special case for new sequence
            prev_sequence = dictionary[previous_code]
            current_sequence = prev_sequence + bytes([prev_sequence[0]])
        else:
            raise ValueError(f"Invalid compressed data at index {index}")
        
        # Add current sequence to result
        result.extend(current_sequence)
        
        # Add to dictionary if possible
        if previous_code is not None and next_code < 65536:
            prev_sequence = dictionary[previous_code]
            new_sequence = prev_sequence + bytes([current_sequence[0]])
            dictionary[next_code] = new_sequence
            next_code += 1
        
        # Update previous code
        previous_code = current_code
    
    return bytes(result)