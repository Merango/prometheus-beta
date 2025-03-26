import pytest
from src.unique_sorted_list import get_unique_sorted_integers

def test_basic_unique_sorted_list():
    """Test basic functionality with a mixed list of integers."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = [1, 2, 3, 4, 5, 6, 9]
    assert get_unique_sorted_integers(input_list) == expected

def test_already_sorted_list():
    """Test a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert get_unique_sorted_integers(input_list) == [1, 2, 3, 4, 5]

def test_list_with_duplicates():
    """Test a list with multiple duplicates."""
    input_list = [5, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]
    assert get_unique_sorted_integers(input_list) == [1, 2, 3, 4, 5]

def test_empty_list():
    """Test an empty list."""
    input_list = []
    assert get_unique_sorted_integers(input_list) == []

def test_negative_numbers():
    """Test a list with negative numbers."""
    input_list = [-3, -1, 0, 2, -2, 1]
    assert get_unique_sorted_integers(input_list) == [-3, -2, -1, 0, 1, 2]

def test_invalid_input_not_list():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        get_unique_sorted_integers("not a list")

def test_invalid_input_non_integers():
    """Test that a TypeError is raised for non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        get_unique_sorted_integers([1, 2, "3", 4])

def test_single_element_list():
    """Test a list with a single element."""
    input_list = [42]
    assert get_unique_sorted_integers(input_list) == [42]