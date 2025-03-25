import pytest
from src.longest_common_subsequence import longest_common_subsequence

def test_basic_subsequence():
    """Test a basic scenario with a clear common subsequence."""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"

def test_no_common_subsequence():
    """Test strings with no common subsequence."""
    assert longest_common_subsequence("XYZ", "ABC") == ""

def test_identical_strings():
    """Test when both strings are identical."""
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_one_empty_string():
    """Test when one string is empty."""
    assert longest_common_subsequence("", "ABC") == ""
    assert longest_common_subsequence("XYZ", "") == ""

def test_both_empty_strings():
    """Test when both strings are empty."""
    assert longest_common_subsequence("", "") == ""

def test_partial_match():
    """Test strings with partial matching characters."""
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_case_sensitivity():
    """Test that the function is case-sensitive."""
    assert longest_common_subsequence("AbC", "aBc") == ""
    assert longest_common_subsequence("Hello", "hello") == ""

def test_special_characters():
    """Test with strings containing special characters."""
    assert longest_common_subsequence("a!b@c", "x!y@z") == "!@"