import pytest
from src.missing_numbers import find_missing_numbers

def test_missing_numbers_ascending():
    """Test finding missing numbers in an ascending array."""
    assert find_missing_numbers([1, 3, 5, 7]) == [2, 4, 6]

def test_missing_numbers_descending():
    """Test finding missing numbers in a descending array."""
    assert find_missing_numbers([7, 5, 3, 1]) == [6, 4, 2]

def test_no_missing_numbers_ascending():
    """Test an array with no missing numbers (ascending)."""
    assert find_missing_numbers([1, 2, 3, 4, 5]) == []

def test_no_missing_numbers_descending():
    """Test an array with no missing numbers (descending)."""
    assert find_missing_numbers([5, 4, 3, 2, 1]) == []

def test_large_range_ascending():
    """Test finding missing numbers in a larger ascending range."""
    assert find_missing_numbers([1, 3, 5, 10, 11, 13]) == [2, 4, 6, 7, 8, 9, 12]

def test_large_range_descending():
    """Test finding missing numbers in a larger descending range."""
    assert find_missing_numbers([13, 11, 10, 5, 3, 1]) == [12, 9, 8, 7, 6, 4, 2]

def test_single_element():
    """Test an array with a single element."""
    assert find_missing_numbers([5]) == [1, 2, 3, 4]

def test_invalid_input_empty():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError):
        find_missing_numbers([])

def test_invalid_input_non_positive():
    """Test that non-positive integers raise a ValueError."""
    with pytest.raises(ValueError):
        find_missing_numbers([1, 2, -3, 4])

def test_invalid_input_non_integer():
    """Test that non-integer inputs raise a ValueError."""
    with pytest.raises(ValueError):
        find_missing_numbers([1, 2, 3.5, 4])