import pytest
from src.max_subarray import kadane_max_subarray

def test_standard_case():
    """Test with a standard array containing positive and negative numbers."""
    assert kadane_max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_all_positive():
    """Test with an array of all positive numbers."""
    assert kadane_max_subarray([1, 2, 3, 4, 5]) == 15

def test_all_negative():
    """Test with an array of all negative numbers."""
    assert kadane_max_subarray([-1, -2, -3, -4, -5]) == -1

def test_single_element():
    """Test with a single element array."""
    assert kadane_max_subarray([42]) == 42

def test_mixed_array():
    """Test with a mixed array of positive and negative numbers."""
    assert kadane_max_subarray([-1, 3, -2, 4, -1]) == 5

def test_zero_sum():
    """Test an array where max sum is zero."""
    assert kadane_max_subarray([-1, -1, 0, -1, -1]) == 0

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        kadane_max_subarray("not a list")

def test_empty_list():
    """Test that ValueError is raised for empty list."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        kadane_max_subarray([])