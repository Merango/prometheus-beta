import pytest
from src.extract_numbers import extract_numbers

def test_extract_numbers_basic():
    """Test extracting numbers from a simple string."""
    assert extract_numbers("I have 42 apples") == [42]

def test_extract_numbers_multiple():
    """Test extracting multiple numbers from a string."""
    assert extract_numbers("I have 42 apples and 7 oranges") == [42, 7]

def test_extract_numbers_no_numbers():
    """Test extracting from a string with no numbers."""
    assert extract_numbers("No numbers here") == []

def test_extract_numbers_negative():
    """Test extracting negative numbers."""
    assert extract_numbers("Negative numbers -123 and 456") == [-123, 456]

def test_extract_numbers_mixed_text():
    """Test extracting numbers from a string with mixed text and numbers."""
    assert extract_numbers("Price: $50, Quantity: 3, Discount: -10%") == [50, 3, -10]

def test_extract_numbers_floating_point_ignored():
    """Test that floating point numbers are not extracted."""
    assert extract_numbers("Temperature: 98.6 degrees") == [98, 6]

def test_extract_numbers_empty_string():
    """Test extracting numbers from an empty string."""
    assert extract_numbers("") == []

def test_extract_numbers_type_error():
    """Test that a type error is raised for non-string input."""
    with pytest.raises(AttributeError):
        extract_numbers(None)
    with pytest.raises(AttributeError):
        extract_numbers(123)