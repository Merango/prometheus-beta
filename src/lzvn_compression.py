"""
Simplified LZVN-like Compression Algorithm Implementation

This module provides a basic run-length encoding (RLE) based compression approach.
While not a full LZVN implementation, it demonstrates compression principles.
"""

def compress(data):
    """
    Compress input data using a simple run-length encoding approach.
    
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
    
    compressed = bytearray()
    i = 0
    
    while i < len(data):
        # Find run of identical bytes
        run_length = 1
        while (i + run_length < len(data) and 
               data[i] == data[i + run_length] and 
               run_length < 255):
            run_length += 1
        
        if run_length > 3:
            # Encode run-length encoding
            compressed.append(0xFF)  # Special marker
            compressed.append(run_length)
            compressed.append(data[i])
            i += run_length
        else:
            # Literal byte
            compressed.append(data[i])
            i += 1
    
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
    
    decompressed = bytearray()
    i = 0
    
    while i < len(compressed_data):
        if i + 2 < len(compressed_data) and compressed_data[i] == 0xFF:
            # Run-length encoding marker
            run_length = compressed_data[i + 1]
            byte_value = compressed_data[i + 2]
            
            # Add repeated byte sequence
            decompressed.extend([byte_value] * run_length)
            i += 3
        else:
            # Literal byte
            decompressed.append(compressed_data[i])
            i += 1
    
    return bytes(decompressed)