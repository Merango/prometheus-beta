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

    # Generate all possible subset sums
    possible_sums = {0}
    for num in numbers:
        # Create a new set of sums to avoid modifying during iteration
        new_sums = set(possible_sums)
        for current_sum in possible_sums:
            new_sum = current_sum + num
            if new_sum <= target_sum:
                new_sums.add(new_sum)
        possible_sums = new_sums

    # Check if the target sum is achievable
    return 1 if target_sum in possible_sums else 0