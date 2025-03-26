import pytest
from src.delete_duplicates import deleteDuplicates

def test_delete_duplicates_basic():
    """Test basic functionality of removing duplicates."""
    assert deleteDuplicates([1, 2, 3, 2, 1, 5, 6, 5, 5, 7]) == [1, 2, 3, 5, 6, 7]

def test_delete_duplicates_empty_list():
    """Test with an empty list."""
    assert deleteDuplicates([]) == []

def test_delete_duplicates_all_same():
    """Test list with all identical elements."""
    assert deleteDuplicates([1, 1, 1, 1]) == [1]

def test_delete_duplicates_already_unique():
    """Test list with no duplicates."""
    assert deleteDuplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_delete_duplicates_order_preservation():
    """Ensure that the order of first occurrence is preserved."""
    input_list = [5, 2, 3, 2, 5, 1, 3, 4]
    expected_output = [5, 2, 3, 1, 4]
    assert deleteDuplicates(input_list) == expected_output

def test_delete_duplicates_large_list():
    """Test with a larger list of mixed unique and duplicate elements."""
    input_list = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
    expected_output = [10, 20, 30, 50, 60, 40, 80]
    assert deleteDuplicates(input_list) == expected_output