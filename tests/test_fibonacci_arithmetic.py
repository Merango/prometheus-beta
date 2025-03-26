import pytest
from src.fibonacci_arithmetic import find_fibonacci_arithmetic_progression

def test_basic_arithmetic_progression():
    """Test finding a basic arithmetic progression of Fibonacci numbers."""
    result = find_fibonacci_arithmetic_progression(3)
    assert result == [0, 1, 1], f"Expected [0, 1, 1], but got {result}"

def test_longer_arithmetic_progression():
    """Test finding a longer arithmetic progression of Fibonacci numbers."""
    result = find_fibonacci_arithmetic_progression(4)
    assert result == [0, 1, 1, 2], f"Expected [0, 1, 1, 2], but got {result}"

def test_invalid_input_negative():
    """Test that the function raises an error for negative input."""
    with pytest.raises(ValueError, match="n must be a positive integer"):
        find_fibonacci_arithmetic_progression(-1)

def test_invalid_input_zero():
    """Test that the function raises an error for zero input."""
    with pytest.raises(ValueError, match="n must be a positive integer"):
        find_fibonacci_arithmetic_progression(0)

def test_invalid_input_non_integer():
    """Test that the function raises an error for non-integer input."""
    with pytest.raises(ValueError, match="n must be a positive integer"):
        find_fibonacci_arithmetic_progression("3")

def test_larger_arithmetic_progression():
    """Test finding a larger arithmetic progression of Fibonacci numbers."""
    result = find_fibonacci_arithmetic_progression(5)
    # Verify it's 5 elements long
    assert len(result) == 5, f"Expected 5 elements, but got {len(result)}"
    
    # Verify it's a Fibonacci sequence
    for i in range(2, len(result)):
        assert result[i] == result[i-1] + result[i-2], f"Not a Fibonacci sequence at index {i}"

def test_progression_with_higher_n():
    """Test finding an arithmetic progression with a larger n."""
    result = find_fibonacci_arithmetic_progression(6)
    # Verify it's 6 elements long
    assert len(result) == 6, f"Expected 6 elements, but got {len(result)}"
    
    # Verify it's a Fibonacci sequence
    for i in range(2, len(result)):
        assert result[i] == result[i-1] + result[i-2], f"Not a Fibonacci sequence at index {i}"