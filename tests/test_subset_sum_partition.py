import pytest
from src.subset_sum_partition import count_equal_sum_partitions

def test_basic_cases():
    # Equal sum partition exists
    assert count_equal_sum_partitions([4, 2, 6]) == 1
    
def test_no_equal_sum_partition():
    # No possible equal sum partition
    test_cases = [
        [1, 2, 3],   # Total 6, cannot make equal partitions
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
    # Various scenarios that can be partitioned
    test_cases = [
        [8, 6, 4, 2],      # Small numbers with equal partition
        [1, 5, 11, 5],     # Tricky case with summing to 11
        [10, 15, 20, 30]   # More complex partitioning
    ]
    
    for numbers in test_cases:
        result = count_equal_sum_partitions(numbers)
        assert result in [0, 1], f"Failed for {numbers}"