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
    
    # Dynamic programming to find valid subset sums
    def subset_sum_exists(nums, target):
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]
        
        return dp[target]

    # Try all possible subset sizes
    for r in range(1, n // 2 + 1):
        for subset in combinations(numbers, r):
            subset_sum = sum(subset)
            if subset_sum == target_sum:
                complement = tuple(x for x in numbers if x not in subset)
                # Verify if the complement can also sum to the target
                if subset_sum_exists(complement, target_sum):
                    return 1

    return 0