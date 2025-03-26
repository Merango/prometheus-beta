import pytest
from src.subset_sum_partition import count_equal_sum_partitions

def test_basic_scenarios():
    # Test case with no valid partitions
    assert count_equal_sum_partitions([1, 2, 3]) == 0
    
    # Test case with one valid partition
    assert count_equal_sum_partitions([1, 2, 3, 4, 5, 7]) == 1
    
    # More complex scenario
    assert count_equal_sum_partitions([1, 2, 3, 4, 5, 6]) == 1

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
    # Larger list with potential multiple partitions
    assert count_equal_sum_partitions([1, 2, 3, 4, 5, 6, 7, 8]) > 0

def test_asymmetric_numbers():
    # Test with larger, asymmetric numbers
    assert count_equal_sum_partitions([10, 15, 20, 25, 30, 35]) > 0