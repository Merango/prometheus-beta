def longest_parity_subsequence(arr):
    """
    Find the longest subsequence with the same parity (all even or all odd).
    
    Args:
        arr (list): Input list of integers
    
    Returns:
        list: The longest subsequence with consistent parity
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input list is empty
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # If only one element, return it
    if len(arr) == 1:
        return arr
    
    # Find all possible subsequences of the same parity
    even_sequences = []
    current_even = []
    odd_sequences = []
    current_odd = []
    
    for num in arr:
        if num % 2 == 0:
            current_even.append(num)
            current_odd = []
        else:
            current_odd.append(num)
            current_even = []
        
        # Save sequences
        if current_even:
            even_sequences.append(current_even.copy())
        if current_odd:
            odd_sequences.append(current_odd.copy())
    
    # Find the longest sequences
    max_even = max(even_sequences, key=len, default=[])
    max_odd = max(odd_sequences, key=len, default=[])
    
    # If equal length, prefer the sequence that appears first
    if len(max_even) == len(max_odd):
        # Find the first occurrence of each sequence type
        first_even_index = arr.index(max_even[0]) if max_even else float('inf')
        first_odd_index = arr.index(max_odd[0]) if max_odd else float('inf')
        
        return max_even if first_even_index < first_odd_index else max_odd
    
    # Return the longer sequence
    return max_even if len(max_even) >= len(max_odd) else max_odd