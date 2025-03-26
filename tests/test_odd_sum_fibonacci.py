import pytest
from src.odd_sum_fibonacci import generate_odd_sum_fibonacci

def test_generate_odd_sum_fibonacci_basic():
    """Test basic functionality of the sequence generator."""
    result = generate_odd_sum_fibonacci(5)
    assert result == [0, 1, 1, 2, 3], f"Expected [0, 1, 1, 2, 3], but got {result}"

def test_generate_odd_sum_fibonacci_edge_cases():
    """Test edge cases: empty sequence, single term, etc."""
    assert generate_odd_sum_fibonacci(0) == [], "Empty sequence should return empty list"
    assert generate_odd_sum_fibonacci(1) == [0], "Single term sequence should be [0]"
    assert generate_odd_sum_fibonacci(2) == [0, 1], "Two-term sequence should be [0, 1]"

def test_generate_odd_sum_fibonacci_odd_sum_property():
    """Verify that the sum of any two consecutive terms is always odd."""
    sequence = generate_odd_sum_fibonacci(10)
    
    # Check odd sum property for each pair of consecutive terms
    for i in range(1, len(sequence)):
        assert (sequence[i-1] + sequence[i]) % 2 == 1, \
            f"Sum of {sequence[i-1]} and {sequence[i]} is not odd"

def test_generate_odd_sum_fibonacci_invalid_input():
    """Test handling of invalid input."""
    with pytest.raises(ValueError, match="Number of terms must be non-negative"):
        generate_odd_sum_fibonacci(-1)

def test_generate_odd_sum_fibonacci_larger_sequence():
    """Test generation of a larger sequence."""
    sequence = generate_odd_sum_fibonacci(8)
    assert len(sequence) == 8, f"Expected sequence of length 8, got {len(sequence)}"
    
    # Additional verification of sequence properties
    expected_start = [0, 1, 1, 2, 3, 5, 8, 13]
    assert sequence == expected_start, f"Unexpected sequence: {sequence}"