import pytest
from src.remove_unique_elements import remove_unique_elements

def test_remove_unique_elements_basic():
    """Test basic functionality of removing unique elements."""
    input_list = [1, 2, 3, 2, 4, 1, 5]
    expected = [1, 2, 2, 1]
    assert remove_unique_elements(input_list) == expected

def test_remove_unique_elements_no_duplicates():
    """Test when no elements are duplicated."""
    input_list = [1, 2, 3, 4, 5]
    expected = []
    assert remove_unique_elements(input_list) == expected

def test_remove_unique_elements_empty_list():
    """Test with an empty list."""
    input_list = []
    expected = []
    assert remove_unique_elements(input_list) == expected

def test_remove_unique_elements_all_duplicates():
    """Test when all elements are duplicates."""
    input_list = [1, 1, 1, 1]
    expected = [1, 1, 1, 1]
    assert remove_unique_elements(input_list) == expected

def test_remove_unique_elements_mixed_types():
    """Test with multiple occurrences of the same value."""
    input_list = [1, 1, 2, 2, 3, 4, 4, 4, 5]
    expected = [1, 1, 2, 2, 4, 4, 4]
    assert remove_unique_elements(input_list) == expected