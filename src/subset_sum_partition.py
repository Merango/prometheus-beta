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

    # Try different subset combinations
    for r in range(1, n // 2 + 1):
        for subset in combinations(numbers, r):
            if sum(subset) == target_sum:
                # Check the complement subset
                complement = [x for x in numbers if x not in subset]
                if sum(complement) == target_sum:
                    return 1

    return 0