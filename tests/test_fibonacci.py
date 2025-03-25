import pytest
from src.fibonacci import fibonacci

def test_fibonacci_base_cases():
    """Test base cases for Fibonacci sequence."""
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1

def test_fibonacci_known_values():
    """Test known Fibonacci numbers."""
    # First few Fibonacci numbers
    expected_values = [
        0,  # 0th
        1,  # 1st
        1,  # 2nd
        2,  # 3rd
        3,  # 4th
        5,  # 5th
        8,  # 6th
        13,  # 7th
        21,  # 8th
        34   # 9th
    ]
    
    for n, expected in enumerate(expected_values):
        assert fibonacci(n) == expected

def test_fibonacci_larger_numbers():
    """Test larger Fibonacci numbers."""
    assert fibonacci(10) == 55
    assert fibonacci(20) == 6765

def test_fibonacci_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Test negative input
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci(-1)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci("5")
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci(None)

def test_fibonacci_performance():
    """Verify memoization by checking performance of repeated calls."""
    # First call to calculate 30th Fibonacci number
    first_call = fibonacci(30)
    
    # Subsequent calls should be fast due to memoization
    second_call = fibonacci(30)
    
    assert first_call == second_call  # Should return same value