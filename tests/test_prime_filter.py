import pytest
from src.prime_filter import filter_primes

def test_basic_prime_filtering():
    """Test filtering a list with mixed prime and non-prime numbers."""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [2, 3, 5, 7]
    assert filter_primes(input_list) == expected

def test_empty_list():
    """Test filtering an empty list."""
    assert filter_primes([]) == []

def test_no_primes():
    """Test a list with no prime numbers."""
    input_list = [1, 4, 6, 8, 9, 10]
    assert filter_primes(input_list) == []

def test_only_primes():
    """Test a list containing only prime numbers."""
    input_list = [2, 3, 5, 7, 11, 13]
    assert filter_primes(input_list) == input_list

def test_large_primes():
    """Test filtering larger prime numbers."""
    input_list = [17, 19, 23, 29, 100, 200]
    expected = [17, 19, 23, 29]
    assert filter_primes(input_list) == expected

def test_invalid_input_type():
    """Test that a non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        filter_primes(42)

def test_non_integer_elements():
    """Test that a list with non-integer elements raises a TypeError."""
    with pytest.raises(TypeError):
        filter_primes([1, 2, 3, 'a', 5])

def test_negative_numbers():
    """Test filtering a list with negative numbers."""
    input_list = [-7, -5, -3, -2, -1, 0, 1, 2, 3, 5, 7]
    expected = [2, 3, 5, 7]
    assert filter_primes(input_list) == expected