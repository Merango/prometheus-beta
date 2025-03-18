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
    Compress input data using a variant of Lempel-Ziv compression.
    
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
    current_pos = 0
    window_size = 4096
    
    while current_pos < len(data):
        # Find longest match in the sliding window
        best_match_length = 0
        best_match_offset = 0
        
        # Limit lookback to avoid excessive computation
        look_back_limit = max(0, current_pos - window_size)
        
        # Search for longest match
        for back_pos in range(current_pos - 1, look_back_limit - 1, -1):
            match_length = 0
            
            # Check match length
            while (current_pos + match_length < len(data) and 
                   match_length < 255 and 
                   data[back_pos + match_length] == data[current_pos + match_length]):
                match_length += 1
            
            # Update best match if longer
            if match_length > best_match_length:
                best_match_length = match_length
                best_match_offset = current_pos - back_pos - 1
        
        # Encode match or literal
        if best_match_length > 2:
            # Encode match: 2 bytes offset, 1 byte length
            compressed.append(best_match_offset >> 8)   # High byte
            compressed.append(best_match_offset & 0xFF) # Low byte
            compressed.append(best_match_length)
            current_pos += best_match_length
        else:
            # Encode literal
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
        # Check if enough data for potential match
        if current_pos + 2 < len(compressed_data):
            # Compute match or literal
            high_byte = compressed_data[current_pos]
            low_byte = compressed_data[current_pos + 1]
            length = compressed_data[current_pos + 2]
            
            # Compute offset
            offset = (high_byte << 8) | low_byte
            
            # Validate match
            if offset > 0 and length > 0 and offset <= len(decompressed):
                # Valid match found
                start_index = len(decompressed) - offset
                
                # Copy match sequence
                match_sequence = bytearray()
                for _ in range(length):
                    if 0 <= start_index < len(decompressed):
                        match_sequence.append(decompressed[start_index])
                        start_index += 1
                    else:
                        # Use last byte added or 0
                        match_byte = match_sequence[-1] if match_sequence else 0
                        match_sequence.append(match_byte)
                
                # Extend decompressed data
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
    
    return bytes(decompressed)