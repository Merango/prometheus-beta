from typing import List, Set
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
        ValueError: If the input list is empty or contains duplicates.
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
    count = 0

    # Use combinations to find valid partitions
    for r in range(1, n // 2 + 1):
        for subset in combinations(numbers, r):
            if sum(subset) == target_sum:
                # Verify the complement subset sums to the same value
                complement = tuple(x for x in numbers if x not in subset)
                if sum(complement) == target_sum:
                    count += 1

    return count