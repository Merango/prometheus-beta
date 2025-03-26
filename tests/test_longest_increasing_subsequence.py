import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from longest_increasing_subsequence import find_longest_increasing_subsequence

def test_normal_increasing_sequence():
    """Test a standard increasing sequence"""
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    assert find_longest_increasing_subsequence(arr) == [10, 22, 33, 50, 60, 80]

def test_empty_list():
    """Test empty list input"""
    assert find_longest_increasing_subsequence([]) == []

def test_single_element_list():
    """Test list with a single element"""
    assert find_longest_increasing_subsequence([5]) == [5]

def test_already_sorted_list():
    """Test a list that is already sorted"""
    arr = [1, 2, 3, 4, 5]
    assert find_longest_increasing_subsequence(arr) == [1, 2, 3, 4, 5]

def test_reverse_sorted_list():
    """Test a list sorted in descending order"""
    arr = [5, 4, 3, 2, 1]
    assert find_longest_increasing_subsequence(arr) == [5]

def test_multiple_possible_subsequences():
    """Test a list with multiple possible longest increasing subsequences"""
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    assert find_longest_increasing_subsequence(arr) == [0, 2, 6, 9, 13, 15]

def test_invalid_input_type():
    """Test error handling for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_longest_increasing_subsequence("not a list")

def test_invalid_list_elements():
    """Test error handling for non-integer list elements"""
    with pytest.raises(ValueError, match="All elements must be integers"):
        find_longest_increasing_subsequence([1, 2, "3", 4])