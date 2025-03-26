from typing import List
from itertools import combinations

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

    # Strict check using combinations
    def strict_subset_check(nums):
        """Comprehensive check for exact subset sum"""
        for r in range(1, len(nums) // 2 + 1):
            for subset in combinations(nums, r):
                subset_sum = sum(subset)
                if subset_sum == target_sum:
                    # Verify complement also sums to target
                    complement = [x for x in nums if x not in subset]
                    if sum(complement) == target_sum:
                        return True
        return False

    return 1 if strict_subset_check(numbers) else 0