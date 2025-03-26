import pytest
from src.anagram_validator import is_anagram

def test_valid_anagrams():
    """Test known valid anagram pairs."""
    assert is_anagram("listen", "silent") == True
    assert is_anagram("hello", "olleh") == True
    assert is_anagram("python", "typhon") == True

def test_non_anagrams():
    """Test strings that are not anagrams."""
    assert is_anagram("test", "best") == False
    assert is_anagram("hello", "world") == False
    assert is_anagram("python", "java") == False

def test_different_lengths():
    """Test strings of different lengths."""
    assert is_anagram("short", "shorter") == False
    assert is_anagram("a", "b") == False

def test_empty_strings():
    """Test empty string edge cases."""
    with pytest.raises(ValueError):
        is_anagram("", "")

def test_single_character():
    """Test single character anagrams."""
    assert is_anagram("a", "a") == True

def test_invalid_input_uppercase():
    """Test that uppercase letters raise a ValueError."""
    with pytest.raises(ValueError):
        is_anagram("Hello", "olleh")

def test_invalid_input_mixed_case():
    """Test that mixed case letters raise a ValueError."""
    with pytest.raises(ValueError):
        is_anagram("Hello", "OLLEH")

def test_invalid_input_with_spaces():
    """Test that inputs with spaces raise a ValueError."""
    with pytest.raises(ValueError):
        is_anagram("hello world", "world hello")

def test_invalid_input_with_special_chars():
    """Test that inputs with special characters raise a ValueError."""
    with pytest.raises(ValueError):
        is_anagram("hello!", "olleh!")