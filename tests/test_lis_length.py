import pytest
from src.lis_length import longest_increasing_subsequence_length

def test_normal_sequence():
    """Test a typical increasing subsequence."""
    assert longest_increasing_subsequence_length([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 6

def test_empty_list():
    """Test an empty list returns 0."""
    assert longest_increasing_subsequence_length([]) == 0

def test_single_element():
    """Test a list with a single element."""
    assert longest_increasing_subsequence_length([5]) == 1

def test_all_equal_elements():
    """Test a list with all equal elements."""
    assert longest_increasing_subsequence_length([3, 3, 3, 3]) == 1

def test_strictly_increasing():
    """Test a strictly increasing sequence."""
    assert longest_increasing_subsequence_length([1, 2, 3, 4, 5]) == 5

def test_decreasing_sequence():
    """Test a strictly decreasing sequence."""
    assert longest_increasing_subsequence_length([5, 4, 3, 2, 1]) == 1

def test_mixed_sequence():
    """Test a mixed sequence."""
    assert longest_increasing_subsequence_length([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6

def test_invalid_input():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError):
        longest_increasing_subsequence_length("not a list")
    with pytest.raises(TypeError):
        longest_increasing_subsequence_length(123)