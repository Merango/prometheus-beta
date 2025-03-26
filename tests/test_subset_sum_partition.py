import pytest
from src.subset_sum_partition import count_equal_sum_partitions

def test_basic_case():
    # Equal sum partition exists
    assert count_equal_sum_partitions([4, 2, 6]) == 1

def test_no_equal_sum_partition():
    # No possible equal sum partition
    assert count_equal_sum_partitions([1, 2, 3]) == 0

def test_edge_cases():
    # Empty list
    assert count_equal_sum_partitions([]) == 0
    
    # Single element list
    assert count_equal_sum_partitions([1]) == 0
    
    # Odd sum total
    assert count_equal_sum_partitions([1, 2]) == 0

def test_error_conditions():
    # Test duplicate numbers
    with pytest.raises(ValueError, match="Input list must contain distinct numbers"):
        count_equal_sum_partitions([1, 1, 2, 3])

def test_various_scenarios():
    # Various scenarios
    test_cases = [
        ([8, 6, 4, 2], 1),      # Small numbers with equal partition
        ([10, 15, 20, 30], 1),  # Medium numbers with equal partition
        ([10, 20, 30, 40, 50, 60], 1)  # Larger numbers with partition
    ]
    
    for numbers in test_cases:
        assert count_equal_sum_partitions(numbers) >= 0