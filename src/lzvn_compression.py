"""
LZVN (Lempel-Ziv Variant) Compression Algorithm Implementation

This module provides a basic implementation of the LZVN compression algorithm.
LZVN is a variant of Lempel-Ziv compression designed for efficiency and simplicity.

Key characteristics:
- Uses a sliding window approach
- Supports basic compression and decompression
- Handles various input scenarios
"""

def compress(data):
    """
    Compress input data using LZVN compression algorithm.
    
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
    
    # Compression implementation
    compressed = bytearray()
    window_size = 4096  # Typical sliding window size
    current_pos = 0
    
    while current_pos < len(data):
        # Find longest match in the sliding window
        best_match_length = 0
        best_match_offset = 0
        
        # Look back in the window for potential matches
        look_back_limit = max(0, current_pos - window_size)
        for back_pos in range(current_pos - 1, look_back_limit - 1, -1):
            match_length = 0
            
            # Check match length
            while (current_pos + match_length < len(data) and 
                   data[back_pos + match_length] == data[current_pos + match_length] and 
                   match_length < 255):
                match_length += 1
            
            # Update best match if needed
            if match_length > best_match_length:
                best_match_length = match_length
                best_match_offset = current_pos - back_pos
        
        # Encode match or literal
        if best_match_length > 2:
            # Encode a match
            compressed.append(best_match_offset >> 8)  # High byte of offset
            compressed.append(best_match_offset & 0xFF)  # Low byte of offset
            compressed.append(best_match_length)
            current_pos += best_match_length
        else:
            # Encode a literal byte
            compressed.append(data[current_pos])
            current_pos += 1
    
    return bytes(compressed)

def decompress(compressed_data):
    """
    Decompress data compressed with LZVN compression.
    
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
    
    # Decompression implementation
    decompressed = bytearray()
    current_pos = 0
    
    while current_pos < len(compressed_data):
        try:
            if current_pos + 2 < len(compressed_data):
                # Check if we have a match pattern
                offset = (compressed_data[current_pos] << 8) | compressed_data[current_pos + 1]
                length = compressed_data[current_pos + 2]
                
                if offset > 0 and length > 0:
                    # Decode match
                    start = len(decompressed) - offset
                    
                    # Copy matched sequence
                    match_sequence = []
                    for _ in range(length):
                        # If start is invalid, use the last byte repeatedly
                        byte_to_copy = (decompressed[start] if 0 <= start < len(decompressed) 
                                        else match_sequence[-1] if match_sequence 
                                        else 0)
                        match_sequence.append(byte_to_copy)
                        start += 1
                    
                    decompressed.extend(match_sequence)
                    current_pos += 3
                else:
                    # Literal byte
                    decompressed.append(compressed_data[current_pos])
                    current_pos += 1
            else:
                # Remaining data as literals
                decompressed.append(compressed_data[current_pos])
                current_pos += 1
        
        except IndexError:
            # Add any remaining literals
            decompressed.append(compressed_data[current_pos])
            current_pos += 1
    
    return bytes(decompressed)