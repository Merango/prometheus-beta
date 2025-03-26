def find_longest_increasing_subsequence(arr):
    """
    Find the longest increasing subsequence in a given array of integers.
    
    Args:
        arr (list): A list of integers to find the longest increasing subsequence in.
    
    Returns:
        list: The longest increasing subsequence.
    
    Raises:
        TypeError: If input is not a list.
        ValueError: If list contains non-integer elements.
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    
    Examples:
        >>> find_longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80])
        [10, 22, 33, 50, 60, 80]
        >>> find_longest_increasing_subsequence([])
        []
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list
    if not arr:
        return []
    
    # Check for non-integer elements
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")
    
    # Length of the input array
    n = len(arr)
    
    # Dynamic Programming approach
    # dp[i] stores the length of LIS ending at index i
    dp = [1] * n
    
    # Previous index tracking for reconstructing the subsequence
    prev = [-1] * n
    
    # Find the longest increasing subsequence
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
    
    # Find the index of the maximum length subsequence
    max_length_index = dp.index(max(dp))
    
    # Reconstruct the subsequence
    subsequence = []
    current = max_length_index
    while current != -1:
        subsequence.insert(0, arr[current])
        current = prev[current]
    
    return subsequence