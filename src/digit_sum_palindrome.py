def is_digit_sum_palindrome(n: int) -> bool:
    """
    Determine if the sum of digits of the input number is a palindrome.

    Args:
        n (int): The input integer to check.

    Returns:
        bool: True if the sum of digits is a palindrome, False otherwise.

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
    
    # Convert sum to string for palindrome check
    sum_str = str(digit_sum)
    
    # Specific handling for small sums
    if digit_sum < 11:
        return digit_sum < 10
    
    # Check if two-digit sum is a palindrome
    return sum_str[0] == sum_str[1] and len(sum_str) == 2