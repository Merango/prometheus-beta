def kadane_max_subarray(arr):
    """
    Compute the maximum sum of a contiguous subarray using Kadane's Algorithm.
    
    Args:
        arr (list): A list of integers to find the maximum subarray sum from.
    
    Returns:
        int: The maximum sum of any contiguous subarray within the input list.
    
    Raises:
        TypeError: If the input is not a list.
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
        raise TypeError("Input must be a list")
    
    if not arr:
        raise ValueError("Input list cannot be empty")
    
    # Initialize variables
    max_sum = current_sum = arr[0]
    
    # Iterate through the array starting from the second element
    for num in arr[1:]:
        # Decide whether to start a new subarray or extend the current one
        current_sum = max(num, current_sum + num)
        
        # Update the maximum sum if the current sum is larger
        max_sum = max(max_sum, current_sum)
    
    return max_sum