import pytest
from src.subset_sum_partition import count_equal_sum_partitions

def test_scenarios_with_partitions():
    # Test cases that can be partitioned into equal sums
    assert count_equal_sum_partitions([1, 2, 3, 4, 5, 6]) == 1
    assert count_equal_sum_partitions([1, 2, 3, 4, 5, 7]) == 0  # Odd total sum

def test_edge_cases():
    # Empty list
    assert count_equal_sum_partitions([]) == 0
    
    # Single element list
    assert count_equal_sum_partitions([1]) == 0
    
    # Two elements making an impossible split
    assert count_equal_sum_partitions([1, 2]) == 0

def test_error_conditions():
    # Test duplicate numbers
    with pytest.raises(ValueError, match="Input list must contain distinct numbers"):
        count_equal_sum_partitions([1, 1, 2, 3])

def test_larger_number_scenarios():
    # Various scenarios
    test_cases = [
        ([10, 20, 30, 40, 50, 60], 1),  # Equal sum partition exists
        ([1, 2, 3], 0),                 # No equal sum partition
        ([3, 1, 1, 2, 2, 3], 0),        # Duplicates not allowed
        ([8, 6, 4, 2], 1)               # Small numbers with equal partition
    ]
    
    for numbers, expected in test_cases:
        assert count_equal_sum_partitions(numbers) == expected