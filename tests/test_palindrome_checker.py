import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindromes():
    """Test basic palindrome scenarios."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True

def test_palindromes_with_spaces_and_punctuation():
    """Test palindromes with spaces and punctuation."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_case_insensitive():
    """Test that palindrome checking is case-insensitive."""
    assert is_palindrome("Racecar") == True
    assert is_palindrome("RaceCar") == True

def test_empty_and_single_char():
    """Test empty string and single character scenarios."""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True

def test_non_palindromes():
    """Test strings that are not palindromes."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        is_palindrome(12345)
    with pytest.raises(TypeError):
        is_palindrome(None)
    with pytest.raises(TypeError):
        is_palindrome(["not", "a", "string"])

def test_unicode_palindromes():
    """Test palindromes with unicode characters."""
    assert is_palindrome("Madam, I'm Adam") == True
    assert is_palindrome("नमन") == True  # Hindi palindrome meaning "salutation"