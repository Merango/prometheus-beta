import pytest
import math
from src.perfect_square import is_perfect_square

def test_perfect_squares():
    """Test known perfect squares."""
    perfect_squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    for num in perfect_squares:
        assert is_perfect_square(num) is True, f"{num} should be a perfect square"

def test_non_perfect_squares():
    """Test numbers that are not perfect squares."""
    non_perfect_squares = [2, 3, 5, 7, 8, 10, 11, 12, 13, 14, 15]
    for num in non_perfect_squares:
        assert is_perfect_square(num) is False, f"{num} should not be a perfect square"

def test_large_perfect_square():
    """Test a large perfect square."""
    large_square = 1000000  # 1000^2
    assert is_perfect_square(large_square) is True

def test_float_perfect_squares():
    """Test float perfect squares."""
    assert is_perfect_square(4.0) is True
    assert is_perfect_square(16.0) is True

def test_float_non_perfect_squares():
    """Test float non-perfect squares."""
    assert is_perfect_square(5.5) is False
    assert is_perfect_square(3.14) is False

def test_zero_and_one():
    """Test edge cases 0 and 1."""
    assert is_perfect_square(0) is True
    assert is_perfect_square(1) is True

def test_negative_input():
    """Test that negative inputs raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative number"):
        is_perfect_square(-4)
    with pytest.raises(ValueError, match="Input must be a non-negative number"):
        is_perfect_square(-1)

def test_invalid_input_type():
    """Test that invalid input types raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be a number"):
        is_perfect_square("16")
    with pytest.raises(TypeError, match="Input must be a number"):
        is_perfect_square([16])
    with pytest.raises(TypeError, match="Input must be a number"):
        is_perfect_square(None)