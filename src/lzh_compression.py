"""
LZH (Lempel-Ziv-Huffman) Compression Algorithm Implementation

This module provides a basic implementation of the LZH compression algorithm.
"""

def encode_varint(value):
    """
    Encode an integer into a variable-length byte sequence.
    
    Args:
        value (int): The integer to encode.
    
    Returns:
        bytes: Encoded integer.
    """
    encoded = []
    while value > 0:
        byte = value & 0x7F
        value >>= 7
        if value > 0:
            byte |= 0x80  # Set continuation bit
        encoded.insert(0, byte)
    
    return bytes(encoded) if encoded else bytes([0])

def decode_varint(data):
    """
    Decode a variable-length byte sequence back to an integer.
    
    Args:
        data (bytes): The byte sequence to decode.
    
    Returns:
        tuple: (decoded integer, number of bytes read)
    """
    value = 0
    bytes_read = 0
    
    for byte in data:
        bytes_read += 1
        value = (value << 7) | (byte & 0x7F)
        if byte & 0x80 == 0:
            break
    
    return value, bytes_read

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
        extended_sequence = current_sequence + bytes([byte])
        
        # If extended sequence is in dictionary, keep extending
        if extended_sequence in dictionary:
            current_sequence = extended_sequence
        else:
            # Output current sequence's code
            current_code = dictionary[current_sequence]
            compressed.extend(encode_varint(current_code))
            
            # If dictionary is not full, add new sequence
            if next_code < 65536:
                dictionary[extended_sequence] = next_code
                next_code += 1
            
            # Reset current sequence to last byte
            current_sequence = bytes([byte])
    
    # Add last sequence if exists
    if current_sequence:
        current_code = dictionary[current_sequence]
        compressed.extend(encode_varint(current_code))
    
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
    
    # Decompression variables
    result = []
    index = 0
    previous_sequence = None
    
    # Decode input completely
    while index < len(compressed_data):
        # Decode next code
        current_code, read_bytes = decode_varint(compressed_data[index:])
        index += read_bytes
        
        # Decode current sequence
        if current_code in dictionary:
            current_sequence = dictionary[current_code]
        else:
            # Special predictive scenario
            if previous_sequence is None:
                raise ValueError("Invalid compressed data")
            
            # Reconstruct sequence
            current_sequence = previous_sequence + bytes([previous_sequence[0]])
        
        # Append current sequence to result
        result.extend(current_sequence)
        
        # Add to dictionary if possible 
        if previous_sequence is not None and next_code < 65536:
            new_sequence = previous_sequence + bytes([current_sequence[0]])
            dictionary[next_code] = new_sequence
            next_code += 1
        
        # Update previous sequence
        previous_sequence = current_sequence
    
    return bytes(result)