import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from bead_sort import bead_sort

def test_bead_sort_normal_case():
    """Test bead sort with a typical list of positive integers."""
    input_list = [5, 3, 1, 4, 2]
    expected = [1, 2, 3, 4, 5]
    assert bead_sort(input_list) == expected

def test_bead_sort_already_sorted():
    """Test bead sort with an already sorted list."""
    input_list = [1, 2, 3, 4, 5]
    assert bead_sort(input_list) == input_list

def test_bead_sort_reverse_sorted():
    """Test bead sort with a reverse-sorted list."""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert bead_sort(input_list) == expected

def test_bead_sort_duplicate_elements():
    """Test bead sort with duplicate elements."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    expected = [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]
    assert bead_sort(input_list) == expected

def test_bead_sort_single_element():
    """Test bead sort with a single-element list."""
    input_list = [42]
    assert bead_sort(input_list) == [42]

def test_bead_sort_empty_list():
    """Test bead sort with an empty list."""
    input_list = []
    assert bead_sort(input_list) == []

def test_bead_sort_input_type_error():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        bead_sort("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        bead_sort(123)

def test_bead_sort_negative_numbers():
    """Test that a ValueError is raised for negative numbers."""
    with pytest.raises(ValueError, match="All elements must be non-negative integers"):
        bead_sort([-1, 2, 3])

def test_bead_sort_non_integer_elements():
    """Test that a ValueError is raised for non-integer elements."""
    with pytest.raises(ValueError, match="All elements must be non-negative integers"):
        bead_sort([1, 2.5, 3])
    with pytest.raises(ValueError, match="All elements must be non-negative integers"):
        bead_sort([1, "2", 3])