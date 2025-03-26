import pytest
from src.palindrome_rearrange import can_form_palindrome, rearrange_to_palindrome

def test_can_form_palindrome_basic():
    assert can_form_palindrome("racecar") == True
    assert can_form_palindrome("hello") == False
    assert can_form_palindrome("aab") == True
    assert can_form_palindrome("") == True

def test_can_form_palindrome_case_insensitive():
    assert can_form_palindrome("RacEcAr") == True
    assert can_form_palindrome("HeLLo") == False

def test_can_form_palindrome_with_spaces():
    assert can_form_palindrome("race car") == True
    assert can_form_palindrome("a man a plan a canal panama") == True

def test_rearrange_to_palindrome_basic():
    assert rearrange_to_palindrome("racecar") == "racecar"
    assert rearrange_to_palindrome("aab") == "aba"
    assert rearrange_to_palindrome("hello") == ""
    assert rearrange_to_palindrome("") == ""

def test_rearrange_to_palindrome_case_sensitivity():
    assert rearrange_to_palindrome("RacEcAr") == "racecar"
    assert rearrange_to_palindrome("AAb") == "aba"

def test_rearrange_to_palindrome_with_spaces():
    assert rearrange_to_palindrome("a man a plan a canal panama") == "amanaplanacanalpanama"

def test_rearrange_to_palindrome_complex_cases():
    assert len(rearrange_to_palindrome("abcdefg")) == 0  # Cannot form palindrome
    assert rearrange_to_palindrome("aabbccddee") in {"abcdedcba", "aabcdedcbaa"}  # Multiple valid palindromes