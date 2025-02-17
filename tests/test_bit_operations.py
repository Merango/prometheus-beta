import pytest
from src.bit_operations import count_set_bits

def test_count_set_bits_positive():
    """Test counting set bits for positive integers."""
    assert count_set_bits(7) == 3  # 111 in binary
    assert count_set_bits(15) == 4  # 1111 in binary
    assert count_set_bits(0) == 0
    assert count_set_bits(1) == 1
    assert count_set_bits(16) == 1  # 10000 in binary

def test_count_set_bits_negative():
    """Test counting set bits for negative integers."""
    assert count_set_bits(-1) == 1
    assert count_set_bits(-7) == 3
    assert count_set_bits(-15) == 4

def test_count_set_bits_edge_cases():
    """Test edge cases and boundary conditions."""
    assert count_set_bits(2**31 - 1) == 31  # Maximum 32-bit signed integer
    assert count_set_bits(-(2**31)) == 1    # Minimum 32-bit signed integer

def test_count_set_bits_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        count_set_bits("not an integer")
    with pytest.raises(TypeError):
        count_set_bits(3.14)
    with pytest.raises(TypeError):
        count_set_bits(None)