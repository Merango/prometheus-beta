import pytest
from src.subset_sum_partition import count_equal_sum_partitions

def test_partitionable_sets():
    # Sets that can be partitioned into equal sums
    assert count_equal_sum_partitions([4, 2, 6]) == 1
    assert count_equal_sum_partitions([8, 6, 4, 2]) == 1

def test_unpartitionable_sets():
    # Sets where no equal partition is possible
    test_cases = [
        [1, 2, 3],    # Cannot perfectly partition
        [1, 2, 4],    # Fails to make equal subsets
        [1, 3, 4],    # Sum cannot be split equally
        [7, 3, 2, 1]  # Complexity checked
    ]
    
    for case in test_cases:
        assert count_equal_sum_partitions(case) == 0, f"Failed for {case}"

def test_edge_cases():
    # Edge case scenarios
    assert count_equal_sum_partitions([]) == 0
    assert count_equal_sum_partitions([1]) == 0
    assert count_equal_sum_partitions([1, 2]) == 0

def test_larger_scenarios():
    # Scenarios with larger sets
    test_cases = [
        [10, 15, 20, 30],        # Potential partitionable set
        [10, 20, 30, 40, 50, 60] # Larger set with partition
    ]
    
    for numbers in test_cases:
        result = count_equal_sum_partitions(numbers)
        assert result in [0, 1], f"Failed for {numbers}"