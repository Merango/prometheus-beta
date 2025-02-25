import pytest
from src.digit_sum_palindrome import is_digit_sum_palindrome

def test_digit_sum_palindrome_true_cases():
    """Test cases where the digit sum is a palindrome."""
    assert is_digit_sum_palindrome(56) == True   # 5+6 = 11
    assert is_digit_sum_palindrome(0) == True    # 0 is a palindrome

def test_digit_sum_palindrome_false_cases():
    """Test cases where the digit sum is not a palindrome."""
    assert is_digit_sum_palindrome(98) == False  # 9+8 = 17
    assert is_digit_sum_palindrome(123) == False  # 1+2+3 = 6
    assert is_digit_sum_palindrome(10) == False  # 1+0 = 1
    assert is_digit_sum_palindrome(99) == False  # 9+9 = 18
    assert is_digit_sum_palindrome(11) == False  # 1+1 = 2

def test_digit_sum_palindrome_negative_input():
    """Test that negative inputs raise a ValueError."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        is_digit_sum_palindrome(-5)

def test_digit_sum_palindrome_large_number():
    """Test a larger number to ensure functionality."""
    assert is_digit_sum_palindrome(1234) == False  # 1+2+3+4 = 10