import pytest
from src.array_logger import log_array_as_table

def test_basic_array_logging():
    """Test logging a simple list of strings"""
    arr = ['apple', 'banana', 'cherry']
    result = log_array_as_table(arr)
    assert 'Value' in result
    assert 'apple' in result
    assert 'banana' in result
    assert 'cherry' in result

def test_array_with_custom_headers():
    """Test logging an array with custom headers"""
    arr = [[1, 2], [3, 4], [5, 6]]
    headers = ['X', 'Y']
    result = log_array_as_table(arr, headers)
    assert 'X' in result
    assert 'Y' in result
    assert '1' in result
    assert '2' in result

def test_nested_array_logging():
    """Test logging a nested array"""
    arr = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25}
    ]
    headers = ['name', 'age']
    result = log_array_as_table(arr, headers)
    assert 'Alice' in result
    assert 'Bob' in result
    assert '30' in result
    assert '25' in result

def test_empty_array():
    """Test logging an empty array"""
    arr = []
    result = log_array_as_table(arr)
    assert result == "Empty array"

def test_array_with_none_values():
    """Test logging an array with None values"""
    arr = [1, None, 3]
    result = log_array_as_table(arr)
    assert 'None' in result

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        log_array_as_table("not a list")

def test_mismatched_headers():
    """Test that ValueError is raised for mismatched headers"""
    arr = [[1, 2], [3, 4]]
    with pytest.raises(ValueError):
        log_array_as_table(arr, headers=['Single'])