import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from tree_sort import tree_sort

def test_basic_sorting():
    """Test sorting of a basic list of integers"""
    input_list = [5, 2, 9, 1, 7, 6]
    assert tree_sort(input_list) == [1, 2, 5, 6, 7, 9]

def test_empty_list():
    """Test sorting of an empty list"""
    assert tree_sort([]) == []

def test_already_sorted_list():
    """Test sorting of an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert tree_sort(input_list) == [1, 2, 3, 4, 5]

def test_reverse_sorted_list():
    """Test sorting of a reverse sorted list"""
    input_list = [5, 4, 3, 2, 1]
    assert tree_sort(input_list) == [1, 2, 3, 4, 5]

def test_list_with_duplicates():
    """Test sorting of a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert tree_sort(input_list) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_list_with_floats():
    """Test sorting of a list with floating point numbers"""
    input_list = [3.14, 2.71, 1.41, 0.58]
    assert tree_sort(input_list) == [0.58, 1.41, 2.71, 3.14]

def test_list_with_negative_numbers():
    """Test sorting of a list with negative numbers"""
    input_list = [-5, 2, -3, 0, 1, -1]
    assert tree_sort(input_list) == [-5, -3, -1, 0, 1, 2]

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        tree_sort("not a list")

def test_unsortable_elements():
    """Test handling of elements that cannot be compared"""
    with pytest.raises(ValueError):
        tree_sort([1, 2, "a", 3])

def test_single_element_list():
    """Test sorting of a list with a single element"""
    input_list = [42]
    assert tree_sort(input_list) == [42]