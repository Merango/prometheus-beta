import pytest
from src.integer_sum import sum_integers

def test_sum_positive_integers():
    """Test summing a list of positive integers"""
    assert sum_integers([1, 2, 3, 4, 5]) == 15

def test_sum_negative_integers():
    """Test summing a list with negative integers"""
    assert sum_integers([-1, -2, -3, -4, -5]) == -15

def test_sum_mixed_integers():
    """Test summing a list with mixed positive and negative integers"""
    assert sum_integers([-1, 0, 1, 2, -2]) == 0

def test_empty_list():
    """Test summing an empty list"""
    assert sum_integers([]) == 0

def test_single_integer():
    """Test summing a list with a single integer"""
    assert sum_integers([42]) == 42

def test_invalid_input_type():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        sum_integers(42)

def test_invalid_element_type():
    """Test raising TypeError for non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        sum_integers([1, 2, '3', 4])