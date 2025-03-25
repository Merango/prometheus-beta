import pytest
from src.palindrome_checker import is_palindrome

def test_basic_palindromes():
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("A") == True

def test_phrase_palindromes():
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_mixed_case_palindromes():
    assert is_palindrome("RaceCar") == True
    assert is_palindrome("Hello") == False

def test_with_numbers():
    assert is_palindrome("12321") == True
    assert is_palindrome("123 321") == True
    assert is_palindrome("12345") == False

def test_empty_and_whitespace():
    assert is_palindrome("") == True
    assert is_palindrome("   ") == True

def test_special_characters():
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car!") == False

def test_unicode_characters():
    assert is_palindrome("Madam, I'm Adam") == True