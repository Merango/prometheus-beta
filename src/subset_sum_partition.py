from typing import List
from itertools import combinations

def count_equal_sum_partitions(numbers: List[int]) -> int:
    """
    Calculate the number of ways a group of numbers can be 
    partitioned into two subsets with equal sums.

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
    
    def can_partition_equally(nums):
        """
        Comprehensive check for a perfect equal sum partition.
        Requires strict matching of both subset sums.
        """
        n = len(nums)
        for r in range(1, n // 2 + 1):
            for subset in combinations(nums, r):
                subset_sum = sum(subset)
                
                # Only proceed if first subset meets target sum exactly
                if subset_sum == target_sum:
                    # Create complement set excluding subset elements
                    complement = [x for x in nums if x not in subset]
                    
                    # Verify complement sums to exactly the same amount
                    if sum(complement) == target_sum:
                        return True
        
        return False

    return 1 if can_partition_equally(numbers) else 0