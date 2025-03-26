from typing import List
from itertools import combinations

def count_equal_sum_partitions(numbers: List[int]) -> int:
    """
    Calculate the number of ways a group of distinct numbers 
    can be partitioned into two subsets with equal sums.

    Args:
        numbers (List[int]): A list of distinct integers to partition.

    Returns:
        int: Number of unique ways to partition the numbers into two 
             subsets with equal total sum.

    Raises:
        ValueError: If the input list contains duplicates.
    """
    # Validate input
    if not numbers:
        return 0
    
    if len(set(numbers)) != len(numbers):
        raise ValueError("Input list must contain distinct numbers")

    total_sum = sum(numbers)
    
    # If total sum is odd, no equal partition is possible
    if total_sum % 2 != 0:
        return 0

    target_sum = total_sum // 2
    n = len(numbers)
    
    # Dynamic programming to solve subset sum problem
    def can_partition_with_subset(subset):
        # Create a DP table to find if the complement can also be partitioned
        complement = [x for x in numbers if x not in subset]
        
        # If complement can't create target sum, return False
        dp = [False] * (target_sum + 1)
        dp[0] = True
        
        for num in complement:
            for j in range(target_sum, num - 1, -1):
                dp[j] |= dp[j - num]
        
        return dp[target_sum]

    # Try all subset combinations
    for r in range(1, n // 2 + 1):
        for subset in combinations(numbers, r):
            if sum(subset) == target_sum:
                if can_partition_with_subset(subset):
                    return 1

    return 0