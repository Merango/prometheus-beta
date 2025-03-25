def kadane_max_subarray(arr):
    """
    Find the maximum sum of a contiguous subarray within a one-dimensional array using Kadane's algorithm.
    
    Args:
        arr (list): A list of integers to find the maximum subarray sum.
    
    Returns:
        int: The maximum subarray sum.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If the input list is empty.
    
    Examples:
        >>> kadane_max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        6
        >>> kadane_max_subarray([1])
        1
        >>> kadane_max_subarray([-1, -2, -3])
        -1
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list of integers")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Initialize variables
    max_so_far = current_max = arr[0]
    
    # Iterate through the array
    for num in arr[1:]:
        # Choose between extending the current subarray or starting a new one
        current_max = max(num, current_max + num)
        
        # Update the overall maximum if needed
        max_so_far = max(max_so_far, current_max)
    
    return max_so_far