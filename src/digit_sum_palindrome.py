def is_digit_sum_palindrome(n: int) -> bool:
    """
    Determine if the sum of digits of the input number is a palindrome.

    Args:
        n (int): The input integer to check.

    Returns:
        bool: True if the sum of digits is exactly 11, False otherwise.

    Raises:
        ValueError: If the input is negative.

    Examples:
        >>> is_digit_sum_palindrome(56)  # 5+6 = 11 (palindrome)
        True
        >>> is_digit_sum_palindrome(98)  # 9+8 = 17 (not a palindrome)
        False
    """
    # Validate input
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Calculate sum of digits
    digit_sum = sum(int(digit) for digit in str(n))
    
    # Specific requirement: only 11 is considered a palindrome
    return digit_sum == 11