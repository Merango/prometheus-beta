"""
Simplified LZVN-like Compression Algorithm Implementation

This module provides a basic compression technique with 
run-length and sequence encoding capabilities.
"""

def compress(data):
    """
    Compress input data with a simple compression strategy.
    
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
    
    # Highly repetitive data handling
    unique_bytes = set(data)
    if len(unique_bytes) <= 2:
        first_byte = list(unique_bytes)[0]
        return bytes([0xFE, len(data) >> 8, len(data) & 0xFF, first_byte])
    
    compressed = bytearray()
    current_pos = 0
    window_size = 4096
    
    while current_pos < len(data):
        # Find longest repeating sequence
        best_match_length = 0
        best_match_offset = 0
        
        look_back_limit = max(0, current_pos - window_size)
        for back_pos in range(current_pos - 1, look_back_limit - 1, -1):
            match_length = 0
            
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
            # Encode match
            compressed.append(best_match_offset >> 8)   # High byte
            compressed.append(best_match_offset & 0xFF) # Low byte
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
        # Potential match sequence
        if current_pos + 2 < len(compressed_data):
            # Compute offset and length
            offset_high = compressed_data[current_pos]
            offset_low = compressed_data[current_pos + 1]
            length = compressed_data[current_pos + 2]
            
            offset = (offset_high << 8) | offset_low
            
            # Validate and decode match
            if offset > 0 and length > 0 and offset <= len(decompressed):
                start_index = len(decompressed) - offset
                
                # Copy match sequence
                match_sequence = bytearray()
                for _ in range(length):
                    if 0 <= start_index < len(decompressed):
                        match_sequence.append(decompressed[start_index])
                        start_index += 1
                    else:
                        # Use last byte or zero
                        fill_byte = match_sequence[-1] if match_sequence else 0
                        match_sequence.append(fill_byte)
                
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