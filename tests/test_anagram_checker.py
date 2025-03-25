import pytest
from src.anagram_checker import anagram_checker

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert anagram_checker("listen", "silent") == True
    assert anagram_checker("triangle", "integral") == True

def test_non_anagrams():
    """Test words that are not anagrams"""
    assert anagram_checker("hello", "world") == False
    assert anagram_checker("python", "java") == False

def test_case_insensitive():
    """Test that the function is case-insensitive"""
    assert anagram_checker("Debit Card", "Bad Credit") == True
    assert anagram_checker("LISTEN", "silent") == True

def test_empty_strings():
    """Test empty string scenarios"""
    assert anagram_checker("", "") == True

def test_whitespace_handling():
    """Test handling of whitespace"""
    assert anagram_checker("astronomer", "moon starer") == True
    assert anagram_checker("  listen  ", "silent") == True

def test_invalid_inputs():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        anagram_checker(123, "hello")
    with pytest.raises(TypeError):
        anagram_checker("hello", None)
    with pytest.raises(TypeError):
        anagram_checker(["list"], "silent")

def test_different_length_words():
    """Test words of different lengths"""
    assert anagram_checker("short", "longer") == False
    assert anagram_checker("a", "ab") == False