"""
Simplified Compression Algorithm 

Provides basic compression with run-length and sequence encoding.
"""

def compress(data):
    """
    Compress input data with basic length-based compression.
    
    Args:
        data (bytes): Input data to be compressed
    
    Returns:
        bytes: Compressed data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If input is empty
    """
    # Input validation
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes")
    
    if not data:
        raise ValueError("Input cannot be empty")
    
    # Detect highly repetitive data
    unique_bytes = set(data)
    if len(unique_bytes) <= 2:
        first_byte = list(unique_bytes)[0]
        return bytes([0xFE, len(data) >> 8, len(data) & 0xFF, first_byte])
    
    compressed = bytearray()
    current_pos = 0
    
    while current_pos < len(data):
        # Find repeated sequences
        run_length = 1
        while (current_pos + run_length < len(data) and 
               data[current_pos] == data[current_pos + run_length] and 
               run_length < 255):
            run_length += 1
        
        if run_length > 3:
            # Encode run-length sequence
            compressed.append(0xFF)  # Special marker
            compressed.append(run_length)
            compressed.append(data[current_pos])
            current_pos += run_length
        else:
            # Literal byte
            compressed.append(data[current_pos])
            current_pos += 1
    
    return bytes(compressed)

def decompress(compressed_data):
    """
    Decompress data compressed with the algorithm.
    
    Args:
        compressed_data (bytes): Data to be decompressed
    
    Returns:
        bytes: Decompressed original data
    
    Raises:
        TypeError: If input is not bytes
        ValueError: If input is empty or corrupted
    """
    # Input validation
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    if not compressed_data:
        raise ValueError("Input cannot be empty")
    
    # Special case for highly repetitive data
    if (len(compressed_data) >= 4 and 
        compressed_data[0] == 0xFE):
        # Decode repetitive sequence
        length = (compressed_data[1] << 8) | compressed_data[2]
        byte_value = compressed_data[3]
        return bytes([byte_value] * length)
    
    decompressed = bytearray()
    current_pos = 0
    
    while current_pos < len(compressed_data):
        # Check for run-length encoding marker
        if (current_pos + 2 < len(compressed_data) and 
            compressed_data[current_pos] == 0xFF):
            # Decode run-length sequence
            run_length = compressed_data[current_pos + 1]
            byte_value = compressed_data[current_pos + 2]
            decompressed.extend([byte_value] * run_length)
            current_pos += 3
        else:
            # Literal byte
            decompressed.append(compressed_data[current_pos])
            current_pos += 1
    
    return bytes(decompressed)