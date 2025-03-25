def longest_increasing_subsequence_length(nums):
    """
    Find the length of the longest increasing subsequence in a list of numbers.
    
    Args:
        nums (list): A list of comparable elements (typically numbers).
    
    Returns:
        int: Length of the longest increasing subsequence.
    
    Raises:
        TypeError: If input is not a list.
        
    Examples:
        >>> longest_increasing_subsequence_length([10, 22, 9, 33, 21, 50, 41, 60, 80])
        6
        >>> longest_increasing_subsequence_length([])
        0
        >>> longest_increasing_subsequence_length([1])
        1
    """
    # Handle edge cases
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    
    if not nums:
        return 0
    
    # Dynamic programming solution
    # dp[i] stores the length of the longest increasing subsequence 
    # that ends with nums[i]
    dp = [1] * len(nums)
    
    # Compute optimal solution
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # Return the maximum length
    return max(dp)