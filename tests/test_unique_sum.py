import pytest
from src.unique_sum import sum_unique_elements

def test_sum_unique_elements_basic():
    """Test basic functionality with a simple list of numbers."""
    assert sum_unique_elements([1, 2, 3, 4, 5]) == 15
    assert sum_unique_elements([1, 1, 2, 2, 3, 3]) == 0
    assert sum_unique_elements([]) == 0

def test_sum_unique_elements_duplicates():
    """Test handling of duplicate elements."""
    assert sum_unique_elements([1, 2, 2, 3, 3, 4]) == 5
    assert sum_unique_elements([5, 5, 5, 5]) == 0
    assert sum_unique_elements([1, 2, 3, 1, 2, 3]) == 0

def test_sum_unique_elements_multiple_duplicates():
    """Test complex scenarios with multiple duplicate occurrences."""
    assert sum_unique_elements([1, 1, 2, 2, 3, 3, 4, 4, 5]) == 5
    assert sum_unique_elements([1, 1, 1, 2, 2, 3, 3, 3]) == 0

def test_sum_unique_elements_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_unique_elements(123)
    
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_unique_elements([1, 2, '3', 4])
    
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_unique_elements([1, 2, 3.5, 4])

def test_sum_unique_elements_large_input():
    """Test function with a larger input to ensure O(n) performance."""
    large_list = list(range(1, 10001)) + list(range(1, 10001))
    assert sum_unique_elements(large_list) == 0