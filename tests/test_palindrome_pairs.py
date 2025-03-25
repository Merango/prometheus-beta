import pytest
from src.palindrome_pairs import find_palindrome_pairs

def test_basic_palindrome_pairs():
    """Test basic palindrome pair scenarios."""
    words = ["bat", "tab", "cat"]
    result = find_palindrome_pairs(words)
    assert sorted(result) == sorted([[0, 1], [1, 0]])

def test_empty_input():
    """Test behavior with empty input list."""
    words = []
    result = find_palindrome_pairs(words)
    assert result == []

def test_single_word():
    """Test behavior with single word."""
    words = ["hello"]
    result = find_palindrome_pairs(words)
    assert result == []

def test_complex_palindrome_pairs():
    """Test more complex palindrome pair scenarios."""
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    result = find_palindrome_pairs(words)
    expected = [[0, 1], [1, 0], [2, 4], [3, 2]]
    assert sorted(result) == sorted(expected)

def test_no_palindrome_pairs():
    """Test scenario with no palindrome pairs."""
    words = ["apple", "banana", "cherry"]
    result = find_palindrome_pairs(words)
    assert result == []

def test_case_sensitive():
    """Ensure case sensitivity is preserved."""
    words = ["Bat", "tab"]
    result = find_palindrome_pairs(words)
    assert result == []  # Case matters

def test_large_input():
    """Test with a larger input set."""
    words = ["a", "b", "c", "ab", "ac", "aa"]
    result = find_palindrome_pairs(words)
    expected = [[2, 4], [4, 2], [0, 5], [5, 0]]
    assert sorted(result) == sorted(expected)