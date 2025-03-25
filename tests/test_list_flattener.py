import pytest
from src.list_flattener import flatten_nested_list

def test_flatten_simple_nested_list():
    """Test flattening a simple nested list."""
    input_list = [1, [2, 3], [4, [5, 6]]]
    expected = [1, 2, 3, 4, 5, 6]
    assert flatten_nested_list(input_list) == expected

def test_flatten_empty_list():
    """Test flattening an empty list."""
    assert flatten_nested_list([]) == []

def test_flatten_no_nesting():
    """Test a list with no nested elements."""
    input_list = [1, 2, 3, 4]
    assert flatten_nested_list(input_list) == input_list

def test_flatten_deeply_nested_list():
    """Test flattening a deeply nested list."""
    input_list = [1, [2, [3, [4, [5]]]], 6]
    expected = [1, 2, 3, 4, 5, 6]
    assert flatten_nested_list(input_list) == expected

def test_flatten_mixed_type_list():
    """Test flattening a list with mixed types."""
    input_list = [1, 'a', [2, 'b'], [3, [4, 'c']]]
    expected = [1, 'a', 2, 'b', 3, 4, 'c']
    assert flatten_nested_list(input_list) == expected

def test_flatten_single_nested_list():
    """Test flattening a single nested list."""
    input_list = [[1, 2]]
    expected = [1, 2]
    assert flatten_nested_list(input_list) == expected

def test_flatten_multiple_levels_of_nesting():
    """Test flattening multiple levels of nested lists."""
    input_list = [1, [2, [3, [4]]], [5, 6]]
    expected = [1, 2, 3, 4, 5, 6]
    assert flatten_nested_list(input_list) == expected