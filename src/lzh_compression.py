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
        current_sequence += bytes([byte])
        
        # If sequence not in dictionary, add to compressed and update dictionary
        if current_sequence not in dictionary:
            # Output the code for the previous sequence
            current_code = dictionary[current_sequence[:-1]]
            compressed.extend(encode_varint(current_code))
            
            # Add new sequence to dictionary if not at max
            if next_code < 65536:  # Limit dictionary size
                dictionary[current_sequence] = next_code
                next_code += 1
            
            # Reset current sequence to last byte
            current_sequence = bytes([byte])
    
    # Add last sequence
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
    
    # Decode first code
    first_code, bytes_read = decode_varint(compressed_data)
    index += bytes_read
    
    # Start with first decoded code
    current = dictionary[first_code]
    result.extend(current)
    
    # Decompress remaining data
    while index < len(compressed_data):
        # Decode next code
        code, read_bytes = decode_varint(compressed_data[index:])
        index += read_bytes
        
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