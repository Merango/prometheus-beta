def run_length_encode(data):
    """
    Implement Run-Length Encoding (RLE) data compression.
    
    Args:
        data (str or list): Input sequence to be encoded
    
    Returns:
        list: Run-length encoded representation
    
    Raises:
        TypeError: If input is not a string or list
        ValueError: If input is an empty sequence
    """
    # Validate input
    if not isinstance(data, (str, list)):
        raise TypeError("Input must be a string or list")
    
    if not data:
        raise ValueError("Input cannot be empty")
    
    # If input is a string, convert to list of characters
    if isinstance(data, str):
        data = list(data)
    
    # Perform run-length encoding
    encoded = []
    current_element = data[0]
    current_count = 1
    
    for item in data[1:]:
        if item == current_element:
            current_count += 1
        else:
            encoded.append((current_element, current_count))
            current_element = item
            current_count = 1
    
    # Add the last run
    encoded.append((current_element, current_count))
    
    return encoded

def run_length_decode(encoded_data):
    """
    Decode a run-length encoded sequence.
    
    Args:
        encoded_data (list): Run-length encoded representation
    
    Returns:
        list: Decoded original sequence
    
    Raises:
        TypeError: If input is not a list of tuples
        ValueError: If input is empty or contains invalid encoding
    """
    # Validate input
    if not isinstance(encoded_data, list):
        raise TypeError("Input must be a list of (element, count) tuples")
    
    if not encoded_data:
        raise ValueError("Input cannot be empty")
    
    # Perform decoding
    decoded = []
    for item, count in encoded_data:
        if not isinstance(count, int) or count < 1:
            raise ValueError(f"Invalid count: {count}. Count must be a positive integer.")
        decoded.extend([item] * count)
    
    return decoded