import pytest
from src.digit_sum import sum_of_digits

def test_sum_of_digits():
    """Test various scenarios for sum_of_digits function."""
    # Test string with all digits
    assert sum_of_digits('1234567890') == 45
    
    # Test string with mixed characters
    assert sum_of_digits('abc123') == 6
    
    # Test string with leading zeros
    assert sum_of_digits('00123') == 6
    
    # Test string with no digits
    assert sum_of_digits('abcdef') == 0
    
    # Test empty string
    assert sum_of_digits('') == 0
    
    # Test string with special characters and digits
    assert sum_of_digits('a1b2c3!@#$%^&*()') == 6
    
    # Test string with large numbers
    assert sum_of_digits('large123number456') == 21
    
    # Test string with repeated digits
    assert sum_of_digits('111222333') == 18