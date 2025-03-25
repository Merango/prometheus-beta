import pytest
from src.string_reversal import recursive_reverse

def test_recursive_reverse_basic():
    """Test basic string reversal"""
    assert recursive_reverse("hello") == "olleh"
    assert recursive_reverse("python") == "nohtyp"

def test_recursive_reverse_empty_string():
    """Test empty string reversal"""
    assert recursive_reverse("") == ""

def test_recursive_reverse_single_char():
    """Test single character string reversal"""
    assert recursive_reverse("a") == "a"

def test_recursive_reverse_palindrome():
    """Test palindrome string reversal"""
    assert recursive_reverse("racecar") == "racecar"

def test_recursive_reverse_with_spaces():
    """Test string reversal with spaces"""
    assert recursive_reverse("hello world") == "dlrow olleh"

def test_recursive_reverse_with_special_chars():
    """Test string reversal with special characters"""
    assert recursive_reverse("a1b2c3") == "3c2b1a"

def test_recursive_reverse_invalid_input():
    """Test error handling for non-string input"""
    with pytest.raises(TypeError):
        recursive_reverse(123)
    
    with pytest.raises(TypeError):
        recursive_reverse(None)
    
    with pytest.raises(TypeError):
        recursive_reverse(["hello"])