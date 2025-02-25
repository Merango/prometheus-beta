import pytest
from src.palindrome_substrings import find_non_overlapping_palindromes

def test_basic_palindromes():
    """Test finding palindromes in a basic string"""
    assert find_non_overlapping_palindromes("abcba") == ["abcba"]

def test_multiple_palindromes():
    """Test finding multiple palindromes"""
    result = find_non_overlapping_palindromes("aabaa")
    assert sorted(result) == ["aa", "aba", "aabaa"]

def test_no_palindromes():
    """Test string with no palindromes"""
    assert find_non_overlapping_palindromes("abcd") == []

def test_empty_string():
    """Test empty string input"""
    assert find_non_overlapping_palindromes("") == []

def test_single_char():
    """Test single character input"""
    assert find_non_overlapping_palindromes("a") == []

def test_mixed_palindromes():
    """Test finding mixed palindromes"""
    result = find_non_overlapping_palindromes("racecar hello radar")
    assert sorted(result) == ["ace", "cec", "hello", "radar", "racecar"]

def test_error_handling():
    """Test error handling for non-string input"""
    with pytest.raises(TypeError):
        find_non_overlapping_palindromes(123)

def test_lexicographic_order():
    """Test that palindromes are returned in lexicographic order"""
    result = find_non_overlapping_palindromes("abcbadad")
    assert result == sorted(result)  # Verify sorting

def test_long_string_palindromes():
    """Test finding palindromes in a longer string"""
    result = find_non_overlapping_palindromes("abcdefgfedcba")
    assert "abcdefgfedcba" in result