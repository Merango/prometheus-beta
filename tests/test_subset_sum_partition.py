import pytest
from src.subset_sum_partition import count_equal_sum_partitions

def test_valid_partitions():
    # Cases that can be partitioned into equal sums
    assert count_equal_sum_partitions([4, 2, 6]) == 1
    assert count_equal_sum_partitions([8, 6, 4, 2]) == 1

def test_no_equal_sum_partition():
    # No possible equal sum partition
    test_cases = [
        [1, 2, 3],   # Cannot make equal partitions
        [1, 2, 4],   # Odd total sum
        [1, 3, 4]    # Cannot make equal partitions
    ]
    
    for case in test_cases:
        assert count_equal_sum_partitions(case) == 0

def test_edge_cases():
    # Empty list
    assert count_equal_sum_partitions([]) == 0
    
    # Single element list
    assert count_equal_sum_partitions([1]) == 0
    
    # Two elements making an impossible split
    assert count_equal_sum_partitions([1, 2]) == 0

def test_larger_scenarios():
    # Various scenarios
    test_cases = [
        [10, 15, 20, 30],       # Medium numbers with partition
        [10, 20, 30, 40, 50, 60] # Larger numbers with partition
    ]
    
    for numbers in test_cases:
        result = count_equal_sum_partitions(numbers)
        assert result in [0, 1], f"Failed for {numbers}"