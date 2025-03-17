import pytest
from src.max_subarray import kadane_max_subarray

def test_standard_array():
    """Test a standard array with mixed positive and negative numbers."""
    assert kadane_max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_all_positive_array():
    """Test an array with all positive numbers."""
    assert kadane_max_subarray([1, 2, 3, 4, 5]) == 15

def test_all_negative_array():
    """Test an array with all negative numbers."""
    assert kadane_max_subarray([-1, -2, -3, -4, -5]) == -1

def test_single_element_array():
    """Test an array with a single element."""
    assert kadane_max_subarray([42]) == 42

def test_zero_elements_array():
    """Test error handling for empty list."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        kadane_max_subarray([])

def test_invalid_input_type():
    """Test error handling for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        kadane_max_subarray("not a list")

def test_array_with_zero():
    """Test an array that includes zero."""
    assert kadane_max_subarray([0, -1, 2, 0]) == 2

def test_alternating_signs():
    """Test an array with alternating positive and negative numbers."""
    assert kadane_max_subarray([1, -1, 2, -2, 3]) == 3