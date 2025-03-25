import pytest
from src.prime_filter import filter_primes

def test_filter_primes_basic():
    """Test basic prime number filtering"""
    assert filter_primes([2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 3, 5, 7]

def test_filter_primes_empty_list():
    """Test filtering an empty list"""
    assert filter_primes([]) == []

def test_filter_primes_no_primes():
    """Test list with no prime numbers"""
    assert filter_primes([1, 4, 6, 8, 9, 10]) == []

def test_filter_primes_negative_numbers():
    """Test filtering prime numbers including negative numbers"""
    assert filter_primes([-2, -3, -4, -5, -6, -7, -8, -9, -10]) == [-2, -3, -5, -7]

def test_filter_primes_mixed_numbers():
    """Test filtering prime numbers from a mixed list of positive and negative numbers"""
    assert filter_primes([-7, 0, 1, 2, 3, 4, 5, -11, 7, 11]) == [2, 3, 5, 7, 11, -7, -11]

def test_filter_primes_edge_cases():
    """Test edge cases like 0, 1, 2"""
    assert filter_primes([0, 1, 2]) == [2]