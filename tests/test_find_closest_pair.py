import pytest
from src.find_closest_pair import find_closest_pair

def test_basic_functionality():
    """Test finding the closest pair in a simple list."""
    assert find_closest_pair([1, 5, 3, 8, 2]) == (1, 2)

def test_negative_numbers():
    """Test finding closest pair with negative numbers."""
    assert find_closest_pair([-1, -5, 3, 8, 2]) == (-1, 2)

def test_duplicate_numbers():
    """Test list with duplicate numbers."""
    assert find_closest_pair([5, 5, 5, 5]) == (5, 5)

def test_tie_breaker():
    """Test that the function returns the pair with smallest numbers in case of a tie."""
    assert find_closest_pair([1, 4, 2, 3]) == (1, 2)

def test_already_sorted():
    """Test a list that's already sorted."""
    assert find_closest_pair([1, 2, 3, 4, 5]) == (1, 2)

def test_reverse_sorted():
    """Test a list sorted in reverse order."""
    assert find_closest_pair([5, 4, 3, 2, 1]) == (1, 2)

def test_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError):
        find_closest_pair([])

def test_single_element_list():
    """Test that a list with only one element raises a ValueError."""
    with pytest.raises(ValueError):
        find_closest_pair([42])

def test_large_numbers():
    """Test with large numbers."""
    assert find_closest_pair([1000000, 1000001, 1, 2]) == (1, 2)

def test_floating_point_numbers():
    """Test with floating point numbers."""
    assert find_closest_pair([1.1, 1.2, 5.5, 8.8]) == (1.1, 1.2)