from typing import List

def count_equal_sum_partitions(numbers: List[int]) -> int:
    """
    Calculate the number of ways a group of distinct numbers 
    can be partitioned into two subsets with equal sums.

    Args:
        numbers (List[int]): A list of distinct integers to partition.

    Returns:
        int: Number indicating if an equal sum partition exists.
             1 if a partition exists, 0 otherwise.

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

    # Dynamic programming approach to solve subset sum problem
    def can_partition(nums, target):
        """
        Determine if a subset of nums can sum to target.
        
        Args:
            nums (List[int]): List of numbers
            target (int): Target sum to achieve
        
        Returns:
            bool: True if a subset can sum to target, False otherwise
        """
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]

        return dp[target]

    # Try all subset possibilities
    for i in range(1, 1 << n):
        subset = [numbers[j] for j in range(n) if i & (1 << j)]
        subset_sum = sum(subset)
        
        # Check if the first subset sums to half the total
        if subset_sum == target_sum:
            # Check if the remaining elements can sum to the same target
            complement = [x for x in numbers if x not in subset]
            if can_partition(complement, target_sum):
                return 1

    return 0