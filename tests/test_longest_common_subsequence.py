import pytest
from src.longest_common_subsequence import longest_common_subsequence

def test_basic_subsequence():
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_empty_strings():
    assert longest_common_subsequence("", "") == ""
    assert longest_common_subsequence("hello", "") == ""
    assert longest_common_subsequence("", "world") == ""

def test_identical_strings():
    assert longest_common_subsequence("hello", "hello") == "hello"

def test_no_common_subsequence():
    assert longest_common_subsequence("abc", "xyz") == ""

def test_partial_match():
    assert longest_common_subsequence("abcdef", "acf") == "acf"

def test_case_sensitivity():
    assert longest_common_subsequence("Hello", "hello") == ""
    assert longest_common_subsequence("programming", "Programming") == ""

def test_type_errors():
    with pytest.raises(TypeError):
        longest_common_subsequence(123, "abc")
    with pytest.raises(TypeError):
        longest_common_subsequence("abc", 456)
    with pytest.raises(TypeError):
        longest_common_subsequence(None, "abc")

def test_unicode_strings():
    assert longest_common_subsequence("résumé", "resumption") == "rsum"

def test_complex_subsequence():
    test_cases = [
        ("ABCDGH", "AEDFHR", "ADH"),
        ("GTAB", "GXTXAYB", "GTAB"),
        ("programming", "programming", "programming"),
        ("computer", "commuter", "comuter")
    ]
    for s1, s2, expected in test_cases:
        assert longest_common_subsequence(s1, s2) == expected