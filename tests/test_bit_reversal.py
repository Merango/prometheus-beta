import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from bit_reversal import reverse_bits

def test_reverse_bits_zero():
    """Test bit reversal of 0."""
    assert reverse_bits(0) == 0

def test_reverse_bits_max_32bit():
    """Test bit reversal of the maximum 32-bit unsigned integer."""
    assert reverse_bits(2**32 - 1) == 2**32 - 1

def test_reverse_bits_example_case():
    """Test a specific example case."""
    # Input:  00000010100101000001111010011100
    # Output: 00111001011110000010100101000000
    assert reverse_bits(43261596) == 964176192

def test_reverse_bits_small_number():
    """Test bit reversal of a small number."""
    assert reverse_bits(1) == 2**31

def test_reverse_bits_invalid_inputs():
    """Test that invalid inputs raise ValueError."""
    with pytest.raises(ValueError):
        reverse_bits(-1)
    
    with pytest.raises(ValueError):
        reverse_bits(2**32)
    
    with pytest.raises(ValueError):
        reverse_bits("not an integer")

def test_reverse_bits_symmetry():
    """Test that reversing bits twice returns the original number."""
    test_numbers = [0, 1, 43261596, 2**32 - 1, 12345]
    for num in test_numbers:
        assert reverse_bits(reverse_bits(num)) == num