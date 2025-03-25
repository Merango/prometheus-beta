import pytest
from src.fibonacci_subsequence import generate_fibonacci_subsequence

def test_zero_input():
    """Test that input 0 returns [0]"""
    assert generate_fibonacci_subsequence(0) == [0]

def test_basic_valid_inputs():
    """Test some basic valid inputs"""
    # Some predefined test cases
    test_cases = [
        (1, [1, 1]),
        (2, [1, 1, 2]),
        (4, [0, 1, 1, 2, 3, 5]),
        (8, [0, 1, 1, 2, 3, 5, 8, 13])
    ]
    
    for target, expected in test_cases:
        result = generate_fibonacci_subsequence(target)
        
        # Verify Fibonacci property
        for i in range(2, len(result)):
            assert result[i] == result[i-1] + result[i-2], f"Not a Fibonacci sequence for input {target}"
        
        # Verify even-indexed sum
        assert sum(result[::2]) == target, f"Even-indexed sum not equal to {target}"

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Negative input
    with pytest.raises(ValueError, match="must be a non-negative integer"):
        generate_fibonacci_subsequence(-1)
    
    # Non-integer input
    with pytest.raises(TypeError, match="must be an integer"):
        generate_fibonacci_subsequence(3.14)
    
    with pytest.raises(TypeError, match="must be an integer"):
        generate_fibonacci_subsequence("5")

def test_impossible_sums():
    """Test some inputs that can't form a valid Fibonacci subsequence"""
    # These are values unlikely to be exactly summed by even-indexed Fibonacci subsequence
    impossible_sums = [7, 15, 100, 1000]
    
    for impossible_sum in impossible_sums:
        with pytest.raises(ValueError, match=f"No Fibonacci subsequence found with even-indexed sum of {impossible_sum}"):
            generate_fibonacci_subsequence(impossible_sum)

def test_subsequence_properties():
    """Additional tests for subsequence properties"""
    def verify_subsequence(result, n):
        # Ensure Fibonacci property
        for i in range(2, len(result)):
            assert result[i] == result[i-1] + result[i-2], "Not a valid Fibonacci sequence"
        
        # Ensure even-indexed sum is correct
        assert sum(result[::2]) == n, "Even-indexed sum is incorrect"
    
    # Test a few more non-trivial cases
    test_cases = [1, 2, 3, 4, 5, 6]
    
    for n in test_cases:
        result = generate_fibonacci_subsequence(n)
        verify_subsequence(result, n)