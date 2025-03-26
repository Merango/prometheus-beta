import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic functionality of removing duplicates"""
    assert remove_duplicates([1, 2, 3, 2, 4, 1, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_empty_list():
    """Test removing duplicates from an empty list"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_all_same():
    """Test a list with all identical elements"""
    assert remove_duplicates([1, 1, 1, 1]) == [1]

def test_remove_duplicates_no_duplicates():
    """Test a list with no duplicates"""
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_preserve_order():
    """Test that the order of first occurrence is preserved"""
    assert remove_duplicates([5, 2, 3, 2, 4, 5, 1]) == [5, 2, 3, 4, 1]

def test_remove_duplicates_with_zero():
    """Test list containing zero with duplicates"""
    assert remove_duplicates([0, 1, 0, 2, 3, 0]) == [0, 1, 2, 3]

def test_remove_duplicates_large_list():
    """Test a larger list with various duplicate patterns"""
    large_list = [1, 2, 3, 4, 5] * 100 + [6, 7, 8]
    expected = [1, 2, 3, 4, 5, 6, 7, 8]
    assert remove_duplicates(large_list) == expected