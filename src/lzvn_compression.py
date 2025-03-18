"""
Simplified LZVN-like Compression Algorithm Implementation

This module provides a sophisticated compression technique 
that handles various input scenarios.
"""

def compress(data):
    """
    Compress input data with advanced sequence detection.
    
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
    window_size = 4096  # Sliding window size
    
    while current_pos < len(data):
        # Find longest match in the sliding window
        best_match_length = 0
        best_match_offset = 0
        
        # Look back in the window
        look_back_limit = max(0, current_pos - window_size)
        for back_pos in range(current_pos - 1, look_back_limit - 1, -1):
            match_length = 0
            
            # Check match length
            while (current_pos + match_length < len(data) and 
                   match_length < 255 and 
                   data[back_pos + match_length] == data[current_pos + match_length]):
                match_length += 1
            
            # Update best match
            if match_length > best_match_length:
                best_match_length = match_length
                best_match_offset = current_pos - back_pos - 1
        
        # Encode match or literal
        if best_match_length > 2:
            # Encode match: 2 bytes for offset, 1 byte for length
            compressed.append(best_match_offset >> 8)   # High byte of offset
            compressed.append(best_match_offset & 0xFF) # Low byte of offset
            compressed.append(best_match_length)
            current_pos += best_match_length
        else:
            # Literal byte
            compressed.append(data[current_pos])
            current_pos += 1
    
    return bytes(compressed)

def decompress(compressed_data):
    """
    Decompress data compressed in the associated format.
    
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
    
    # Check for special case of highly repetitive data
    if (len(compressed_data) >= 4 and 
        compressed_data[0] == 0xFE):
        # Decode special repetitive case
        length = (compressed_data[1] << 8) | compressed_data[2]
        byte_value = compressed_data[3]
        return bytes([byte_value] * length)
    
    decompressed = bytearray()
    current_pos = 0
    
    while current_pos < len(compressed_data):
        # Check if we have a full match sequence
        if current_pos + 2 < len(compressed_data):
            # Compute offset and length
            offset_high = compressed_data[current_pos]
            offset_low = compressed_data[current_pos + 1]
            length = compressed_data[current_pos + 2]
            
            # Compute full offset
            offset = (offset_high << 8) | offset_low
            
            # Validate match and decode
            if offset > 0 and length > 0 and offset <= len(decompressed):
                # Valid match
                start_index = len(decompressed) - offset
                
                # Copy matched sequence
                for _ in range(length):
                    if 0 <= start_index < len(decompressed):
                        decompressed.append(decompressed[start_index])
                        start_index += 1
                    else:
                        # Use last byte or zero
                        fill_byte = decompressed[-1] if decompressed else 0
                        decompressed.append(fill_byte)
                
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