from typing import List, Set
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
    
    def check_subset_sums(nums: List[int], target: int) -> bool:
        """
        Check if a subset exists that sums exactly to the target.
        Use exhaustive combination checking to verify.
        """
        # Cache for unique subset sum approaches
        unique_partition_approaches: Set[frozenset] = set()
        
        for r in range(1, len(nums) // 2 + 1):
            for subset in combinations(nums, r):
                # Compute subset sum
                subset_sum = sum(subset)
                
                # Only proceed if this subset sum matches target
                if subset_sum == target:
                    # Create complement set
                    complement = [x for x in nums if x not in subset]
                    
                    # Verify complement sum matches target
                    if sum(complement) == target:
                        # Use frozenset to handle order-independent uniqueness
                        partition = frozenset([frozenset(subset), frozenset(complement)])
                        unique_partition_approaches.add(partition)
        
        return len(unique_partition_approaches) > 0

    return 1 if check_subset_sums(numbers, target_sum) else 0