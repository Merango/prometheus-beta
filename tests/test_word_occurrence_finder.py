import pytest
from src.word_occurrence_finder import find_word_occurrences

def test_basic_occurrence():
    """Test finding a word with a single occurrence"""
    result = find_word_occurrences("hello world hello", "hello")
    assert result == [(0, "hello"), (11, "hello")]

def test_no_occurrences():
    """Test when target word is not in the string"""
    result = find_word_occurrences("hello world python", "java")
    assert result == []

def test_single_word_string():
    """Test with a single word string"""
    result = find_word_occurrences("python", "python")
    assert result == [(0, "python")]

def test_empty_string_raises_error():
    """Test that empty string raises a ValueError"""
    with pytest.raises(ValueError):
        find_word_occurrences("", "test")

def test_empty_target_word_raises_error():
    """Test that empty target word raises a ValueError"""
    with pytest.raises(ValueError):
        find_word_occurrences("hello world", "")

def test_non_string_input_raises_error():
    """Test that non-string inputs raise a TypeError"""
    with pytest.raises(TypeError):
        find_word_occurrences(123, "test")
    
    with pytest.raises(TypeError):
        find_word_occurrences("hello", 123)

def test_complex_occurrence():
    """Test occurrence in a more complex string"""
    result = find_word_occurrences("the quick brown fox jumps the fox", "fox")
    assert result == [(16, "fox"), (30, "fox")]

def test_case_sensitive():
    """Test that search is case-sensitive"""
    result = find_word_occurrences("Hello hello HELLO", "hello")
    assert result == [(6, "hello")]