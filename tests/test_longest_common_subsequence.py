import pytest
from src.longest_common_subsequence import longest_common_subsequence

def test_basic_lcs():
    """Test basic longest common subsequence scenarios."""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_empty_strings():
    """Test scenarios with empty strings."""
    assert longest_common_subsequence("", "ABC") == ""
    assert longest_common_subsequence("ABC", "") == ""
    assert longest_common_subsequence("", "") == ""

def test_no_common_subsequence():
    """Test strings with no common subsequence."""
    assert longest_common_subsequence("XYZ", "ABC") == ""

def test_identical_strings():
    """Test when both strings are identical."""
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_partial_subsequence():
    """Test partial subsequence scenarios."""
    assert longest_common_subsequence("ABCBDAB", "BDCABA") == "BCBA"

def test_different_lengths():
    """Test strings of different lengths."""
    assert longest_common_subsequence("ABCD", "AD") == "AD"
    assert longest_common_subsequence("AD", "ABCD") == "AD"

def test_case_sensitivity():
    """Test case sensitivity of the function."""
    assert longest_common_subsequence("AbC", "aBc") == "b"

def test_repeated_characters():
    """Test scenarios with repeated characters."""
    assert longest_common_subsequence("AAAAAA", "AAAA") == "AAAA"