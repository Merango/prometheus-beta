import pytest
from src.digit_validator import is_digits_only

def test_valid_digit_strings():
    """Test strings that contain only digits."""
    assert is_digits_only("12345") == True
    assert is_digits_only("0") == True
    assert is_digits_only("9876543210") == True

def test_invalid_digit_strings():
    """Test strings that contain non-digit characters."""
    assert is_digits_only("123a45") == False
    assert is_digits_only("12 345") == False
    assert is_digits_only("12-345") == False
    assert is_digits_only("") == False
    assert is_digits_only("  ") == False

def test_edge_cases():
    """Test edge cases and type checking."""
    # Type checking
    with pytest.raises(TypeError):
        is_digits_only(12345)
    
    with pytest.raises(TypeError):
        is_digits_only(None)
    
    with pytest.raises(TypeError):
        is_digits_only(["1", "2", "3"])

def test_unicode_digits():
    """Test behavior with digit validation.
    
    Note: For this implementation, we specifically want ONLY ASCII digits.
    """
    assert is_digits_only("123٤٥") == False  # Mixed digit systems
    # Unicode digits are not considered valid
    assert is_digits_only("١٢٣") == False  # Arabic digits
    assert is_digits_only("१२३") == False  # Devanagari digits