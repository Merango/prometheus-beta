import pytest
from src.bitwise_and_range import bitwise_and_range

def test_basic_range():
    """Test a basic range of numbers"""
    assert bitwise_and_range(5, 7) == 4

def test_same_number():
    """Test when start and end are the same number"""
    assert bitwise_and_range(10, 10) == 10

def test_consecutive_numbers():
    """Test with consecutive numbers"""
    assert bitwise_and_range(4, 5) == 4

def test_zero_range():
    """Test range starting from zero"""
    assert bitwise_and_range(0, 5) == 0

def test_large_range():
    """Test a larger range of numbers"""
    assert bitwise_and_range(10, 15) == 8

def test_negative_start_raises_error():
    """Test that negative start raises ValueError"""
    with pytest.raises(ValueError, match="Both start and end must be non-negative integers"):
        bitwise_and_range(-1, 5)

def test_negative_end_raises_error():
    """Test that negative end raises ValueError"""
    with pytest.raises(ValueError, match="Both start and end must be non-negative integers"):
        bitwise_and_range(1, -5)

def test_start_greater_than_end_raises_error():
    """Test that start > end raises ValueError"""
    with pytest.raises(ValueError, match="Start must be less than or equal to end"):
        bitwise_and_range(10, 5)