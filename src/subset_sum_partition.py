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

    # Precompute possible sums using dynamic programming
    possible_sums = {0}
    for num in numbers:
        new_sums = set()
        for current_sum in possible_sums:
            new_sum = current_sum + num
            if new_sum <= target_sum:
                new_sums.add(new_sum)
        possible_sums.update(new_sums)

    # Check if the target sum is achievable
    return 1 if target_sum in possible_sums else 0