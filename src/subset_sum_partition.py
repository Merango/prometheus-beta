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

    # Dynamic programming solution
    def backtrack(index, current_sum):
        """Recursive backtracking with memoization"""
        # Reached the end of the array
        if index == n:
            return current_sum == target_sum
        
        # Skip the current number
        if backtrack(index + 1, current_sum):
            return True
        
        # Include the current number
        if current_sum + numbers[index] <= target_sum:
            if backtrack(index + 1, current_sum + numbers[index]):
                return True
        
        return False

    return 1 if backtrack(0, 0) else 0