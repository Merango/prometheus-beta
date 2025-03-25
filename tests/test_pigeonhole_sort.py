import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from pigeonhole_sort import pigeonhole_sort

def test_basic_sorting():
    """Test basic sorting of a list of integers"""
    input_list = [8, 3, 2, 7, 4, 6, 8]
    expected = sorted(input_list)
    assert pigeonhole_sort(input_list) == expected

def test_empty_list():
    """Test sorting an empty list"""
    assert pigeonhole_sort([]) == []

def test_single_element_list():
    """Test sorting a list with a single element"""
    assert pigeonhole_sort([5]) == [5]

def test_already_sorted_list():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert pigeonhole_sort(input_list) == input_list

def test_reverse_sorted_list():
    """Test sorting a list in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert pigeonhole_sort(input_list) == expected

def test_list_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    assert pigeonhole_sort(input_list) == expected

def test_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-5, 3, -2, 0, 7, -1]
    expected = sorted(input_list)
    assert pigeonhole_sort(input_list) == expected

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError, match="Input must be a list"):
        pigeonhole_sort("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        pigeonhole_sort(123)

def test_non_integer_elements():
    """Test that a ValueError is raised for non-integer elements"""
    with pytest.raises(ValueError, match="All elements must be integers"):
        pigeonhole_sort([1, 2, 3, 'a'])
    with pytest.raises(ValueError, match="All elements must be integers"):
        pigeonhole_sort([1.5, 2, 3, 4])

def test_large_range_of_numbers():
    """Test sorting a list with a large range of numbers"""
    input_list = [1000, -1000, 500, -500, 0]
    expected = sorted(input_list)
    assert pigeonhole_sort(input_list) == expected