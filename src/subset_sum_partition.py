from typing import List

def count_equal_sum_partitions(numbers: List[int]) -> int:
    """
    Calculate the number of ways a group of distinct numbers 
    can be partitioned into two subsets with equal sums.

    Args:
        numbers (List[int]): A list of integers to partition.

    Returns:
        int: Number indicating if an equal sum partition exists.
             1 if a partition exists, 0 otherwise.
    """
    # Validate input
    if not numbers:
        return 0

    total_sum = sum(numbers)
    
    # If total sum is odd, no equal partition is possible
    if total_sum % 2 != 0:
        return 0

    target_sum = total_sum // 2
    n = len(numbers)

    # Create a DP table to track possible subset sums
    dp = [[False] * (target_sum + 1) for _ in range(n + 1)]
    
    # 0 sum is always possible
    for i in range(n + 1):
        dp[i][0] = True

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            if j < numbers[i-1]:
                # If current number is larger than current sum
                dp[i][j] = dp[i-1][j]
            else:
                # Either exclude current number or include it
                dp[i][j] = dp[i-1][j] or dp[i-1][j-numbers[i-1]]

    return 1 if dp[n][target_sum] else 0