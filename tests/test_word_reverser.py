import pytest
from src.word_reverser import reverse_words

def test_basic_word_reversal():
    """Test basic word reversal"""
    assert reverse_words("Hello World") == "World Hello"

def test_punctuation_preservation():
    """Test that punctuation is preserved"""
    assert reverse_words("Hello, World!") == "World, Hello!"

def test_mixed_case():
    """Test preservation of original capitalization"""
    assert reverse_words("Python Is AWESOME") == "AWESOME Is Python"

def test_multiple_spaces():
    """Test handling of multiple spaces"""
    assert reverse_words("  Hello   World  ") == "  World   Hello  "

def test_single_word():
    """Test single word input"""
    assert reverse_words("Hello") == "Hello"

def test_empty_string():
    """Test empty string input"""
    assert reverse_words("") == ""

def test_complex_punctuation():
    """Test complex punctuation scenarios"""
    assert reverse_words("a,b c") == "c,b a"
    assert reverse_words("first, second; third.") == "third, second; first."

def test_numbers_and_words():
    """Test mixing numbers and words"""
    assert reverse_words("Hello 123 World") == "World 123 Hello"

def test_symbols():
    """Test with special characters"""
    assert reverse_words("a!b@c#d") == "d!c@b#a"