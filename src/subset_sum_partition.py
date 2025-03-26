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

    # Find a subset that perfectly matches the target sum
    def find_exact_subset(nums, target):
        """
        Find a subset that exactly matches the target sum.
        Use combinations to comprehensively check all possibilities.
        """
        for r in range(1, len(nums) // 2 + 1):
            for subset in combinations(nums, r):
                if sum(subset) == target:
                    # Verify complement sums to the same amount
                    complement = [x for x in nums if x not in subset]
                    if sum(complement) == target:
                        return True
        return False

    return 1 if find_exact_subset(numbers, target_sum) else 0