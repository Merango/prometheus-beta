import pytest
from src.digit_sum_palindrome import is_digit_sum_palindrome

def test_digit_sum_palindrome_true_cases():
    """Test cases where the digit sum is a palindrome."""
    assert is_digit_sum_palindrome(56) == True   # 5+6 = 11
    assert is_digit_sum_palindrome(11) == True   # 1+1 = 2
    assert is_digit_sum_palindrome(0) == True    # 0 is a palindrome
    assert is_digit_sum_palindrome(99) == True   # 9+9 = 18 is not, but 11 is

def test_digit_sum_palindrome_false_cases():
    """Test cases where the digit sum is not a palindrome."""
    assert is_digit_sum_palindrome(98) == False  # 9+8 = 17
    assert is_digit_sum_palindrome(123) == False  # 1+2+3 = 6

def test_digit_sum_palindrome_edge_cases():
    """Test edge cases."""
    assert is_digit_sum_palindrome(10) == False  # 1+0 = 1 (single digit is a palindrome)
    assert is_digit_sum_palindrome(55) == True   # 5+5 = 10 is not, but 11 is

def test_digit_sum_palindrome_negative_input():
    """Test that negative inputs raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        is_digit_sum_palindrome(-5)

def test_digit_sum_palindrome_large_number():
    """Test a larger number to ensure functionality."""
    assert is_digit_sum_palindrome(1234) == False  # 1+2+3+4 = 10