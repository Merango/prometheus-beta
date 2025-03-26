import pytest
from src.subset_sum_partition import count_equal_sum_partitions

def test_scenarios_with_partitions():
    # Test case with one partition
    assert count_equal_sum_partitions([1, 2, 3, 4, 5, 7]) > 0
    
    # More complex scenario
    assert count_equal_sum_partitions([1, 2, 3, 4, 5, 6]) > 0

def test_scenarios_without_partitions():
    # Test case with no valid partitions
    assert count_equal_sum_partitions([1, 2, 3]) == 0
    
    # Odd sum total
    assert count_equal_sum_partitions([1, 2, 4]) == 0

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

def test_more_complex_cases():
    # Larger list with potential partitions
    result = count_equal_sum_partitions([10, 15, 20, 25, 30, 35])
    assert isinstance(result, int)
    assert result >= 0

def test_various_partition_scenarios():
    # Different scenarios to validate the algorithm
    test_cases = [
        ([1, 2, 3, 4, 5, 6], 1),  # Certain numbers can be partitioned
        ([1, 2, 3], 0),            # Cannot be partitioned
        ([5, 5, 5, 5, 5, 5], 0),   # Duplicates not allowed
        ([10, 20, 30, 40, 50, 60], 1)  # Larger numbers with a partition
    ]
    
    for numbers, expected in test_cases:
        assert count_equal_sum_partitions(numbers) == expected