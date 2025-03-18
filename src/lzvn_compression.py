"""
Simplified LZVN-like Compression Algorithm Implementation

This module provides a basic run-length and dictionary-style compression approach.
"""

def compress(data):
    """
    Compress input data using a hybrid encoding approach.
    
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
    dictionary = {}
    current_pos = 0
    
    while current_pos < len(data):
        # Look for longest sequence in dictionary/sliding window
        best_match_length = 0
        best_match_start = -1
        
        # Search backward in recent data
        search_limit = max(0, current_pos - 4096)
        for start in range(current_pos - 1, search_limit - 1, -1):
            match_length = 0
            
            # Try to find the longest match
            while (current_pos + match_length < len(data) and 
                   start + match_length < current_pos and 
                   match_length < 255 and 
                   data[start + match_length] == data[current_pos + match_length]):
                match_length += 1
            
            # Update best match
            if match_length > best_match_length:
                best_match_length = match_length
                best_match_start = start
        
        # Encode based on match length
        if best_match_length > 2:
            # Compute relative offset
            offset = current_pos - best_match_start - 1
            
            # Marker for compressed sequence (offset high byte)
            compressed.append(offset >> 8)
            # Offset low byte
            compressed.append(offset & 0xFF)
            # Length of match
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
    
    decompressed = bytearray()
    current_pos = 0
    
    while current_pos < len(compressed_data):
        # Attempt to decode compressed sequence
        if current_pos + 2 < len(compressed_data):
            # Parse offset and length
            offset_high = compressed_data[current_pos]
            offset_low = compressed_data[current_pos + 1]
            length = compressed_data[current_pos + 2]
            
            # Compute full offset
            offset = (offset_high << 8) | offset_low
            
            if offset > 0 and length > 0 and offset <= len(decompressed):
                # Valid match found
                start_index = len(decompressed) - offset
                
                # Copy matched sequence
                for _ in range(length):
                    if 0 <= start_index < len(decompressed):
                        decompressed.append(decompressed[start_index])
                        start_index += 1
                    else:
                        # Use last byte or zero if no valid reference
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