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
    
    # Find the longest consecutive subsequences of the same parity
    def get_consecutive_subsequences(arr, is_even):
        subsequences = []
        current_seq = []
        for num in arr:
            if (num % 2 == 0) == is_even:
                current_seq.append(num)
            else:
                if current_seq:
                    subsequences.append(current_seq)
                current_seq = []
        if current_seq:
            subsequences.append(current_seq)
        return subsequences
    
    # Get even and odd subsequences
    even_subsequences = get_consecutive_subsequences(arr, True)
    odd_subsequences = get_consecutive_subsequences(arr, False)
    
    # Find the maximum subsequences
    max_even = max(even_subsequences, key=len, default=[])
    max_odd = max(odd_subsequences, key=len, default=[])
    
    # Return the longer subsequence, with preference to odd in case of tie
    if len(max_even) == len(max_odd):
        # Prefer the earlier subsequence
        first_even_index = arr.index(max_even[0]) if max_even else float('inf')
        first_odd_index = arr.index(max_odd[0]) if max_odd else float('inf')
        
        # If starting positions are the same, prefer sequential one
        if first_even_index == first_odd_index:
            return max_odd if len(max_odd) >= 3 else max_even
        
        return max_even if first_even_index < first_odd_index else max_odd
    
    # If lengths differ, return the longer one
    return max_even if len(max_even) >= len(max_odd) else max_odd