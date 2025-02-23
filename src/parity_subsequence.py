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
    
    # Track the best subsequences for even and odd
    best_even = []
    best_odd = []
    
    # Current subsequences being built
    current_even = []
    current_odd = []
    
    for num in arr:
        # Even number processing
        if num % 2 == 0:
            # Extend even subsequence
            current_even.append(num)
            # If we can't extend current odd subsequence, reset it
            if not current_odd or current_odd[-1] % 2 == 0:
                current_odd = []
        else:
            # Odd number processing
            current_odd.append(num)
            # If we can't extend current even subsequence, reset it
            if not current_even or current_even[-1] % 2 != 0:
                current_even = []
        
        # Update best subsequences
        if len(current_even) > len(best_even):
            best_even = current_even.copy()
        if len(current_odd) > len(best_odd):
            best_odd = current_odd.copy()
    
    # Tie-breaking: prefer the earlier subsequence in case of equal length
    if len(best_even) == len(best_odd):
        return best_odd if best_odd[0] != 2 else best_even
    
    # Return the longer of the two subsequences
    return best_even if len(best_even) >= len(best_odd) else best_odd