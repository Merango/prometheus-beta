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
    unique_partitions = set()

    # Use combinations to find valid partitions
    for r in range(1, n // 2 + 1):
        for subset in combinations(numbers, r):
            if sum(subset) == target_sum:
                # Sort the complement to create a unique representation
                complement = tuple(sorted(x for x in numbers if x not in subset))
                if sum(complement) == target_sum:
                    # Use frozenset to handle order-independent uniqueness
                    unique_partitions.add(frozenset([frozenset(subset), frozenset(complement)]))

    return len(unique_partitions)