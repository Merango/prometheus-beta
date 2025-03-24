import pytest
from src.find_occurrences import find_first_last_occurrence

def test_find_occurrences_normal_case():
    """Test finding occurrences in a normal sorted array"""
    arr = [1, 2, 2, 2, 3, 4, 5, 5, 5]
    assert find_first_last_occurrence(arr, 2) == (1, 3)
    assert find_first_last_occurrence(arr, 5) == (6, 8)

def test_find_occurrences_single_element():
    """Test finding occurrences of a single-occurrence element"""
    arr = [1, 2, 3, 4, 5]
    assert find_first_last_occurrence(arr, 3) == (2, 2)

def test_find_occurrences_not_found():
    """Test finding an element not in the array"""
    arr = [1, 2, 3, 4, 5]
    assert find_first_last_occurrence(arr, 6) == (-1, -1)

def test_find_occurrences_empty_array():
    """Test finding an element in an empty array"""
    arr = []
    assert find_first_last_occurrence(arr, 1) == (-1, -1)

def test_find_occurrences_first_element():
    """Test finding the first element in the array"""
    arr = [1, 1, 1, 2, 3, 4]
    assert find_first_last_occurrence(arr, 1) == (0, 2)

def test_find_occurrences_last_element():
    """Test finding the last element in the array"""
    arr = [1, 2, 3, 4, 5, 5, 5]
    assert find_first_last_occurrence(arr, 5) == (4, 6)

def test_find_occurrences_multiple_occurrences():
    """Test finding an element with multiple occurrences"""
    arr = [1, 2, 2, 2, 2, 3, 4, 5]
    assert find_first_last_occurrence(arr, 2) == (1, 4)

def test_find_occurrences_at_array_bounds():
    """Test finding elements at the beginning and end of the array"""
    arr = [1, 1, 2, 3, 4, 5, 5]
    assert find_first_last_occurrence(arr, 1) == (0, 1)
    assert find_first_last_occurrence(arr, 5) == (5, 6)