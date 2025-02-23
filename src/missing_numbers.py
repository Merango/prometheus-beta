def find_missing_numbers(arr):
    """
    Find all missing numbers in a sorted array of positive integers.
    
    Args:
        arr (list): A sorted list of positive integers (ascending or descending).
    
    Returns:
        list: A list of missing numbers between the minimum and maximum values.
    
    Raises:
        ValueError: If the input is not a valid list of positive integers.
    """
    # Validate input
    if not arr or not all(isinstance(x, int) and x > 0 for x in arr):
        raise ValueError("Input must be a non-empty list of positive integers")
    
    # Determine if the array is ascending or descending
    is_ascending = arr[0] <= arr[-1]
    
    # Sort the array in ascending order for consistent processing
    if not is_ascending:
        arr = sorted(arr, reverse=True)
    
    # Find the range of numbers
    min_val = min(arr)
    max_val = max(arr)
    
    # Handle single element case
    if len(arr) == 1:
        # Generate missing numbers from 1 to element-1
        missing = list(range(1, min_val))
    else:
        # Create a set of the input array for efficient lookup
        num_set = set(arr)
        
        # Find missing numbers
        missing = [
            num for num in range(1, max_val + 1) 
            if num not in num_set
        ]
    
    # If the original array was descending, reverse the missing numbers
    return sorted(missing, reverse=not is_ascending)