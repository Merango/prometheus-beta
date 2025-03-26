from collections import Counter

def can_form_palindrome(s: str) -> bool:
    """
    Determines if the characters in the given string can be rearranged to form a palindrome.
    
    Args:
        s (str): Input string to check for palindrome rearrangement possibility
    
    Returns:
        bool: True if characters can be rearranged to form a palindrome, False otherwise
    
    Examples:
        >>> can_form_palindrome("racecar")
        True
        >>> can_form_palindrome("hello")
        False
    """
    # Remove any whitespace and convert to lowercase to normalize input
    s = s.replace(" ", "").lower()
    
    # Count character frequencies
    char_counts = Counter(s)
    
    # Count how many characters have odd frequencies
    odd_count = sum(1 for count in char_counts.values() if count % 2 != 0)
    
    # Palindrome is possible if at most one character has an odd frequency
    return odd_count <= 1

def rearrange_to_palindrome(s: str) -> str:
    """
    Rearranges the characters in the input string to form a palindrome.
    
    Args:
        s (str): Input string to rearrange
    
    Returns:
        str: A palindrome rearranged from the input string, or an empty string if not possible
    
    Examples:
        >>> rearrange_to_palindrome("racecar")
        'racecar'
        >>> rearrange_to_palindrome("aab")
        'aba'
    """
    # Remove whitespace and convert to lowercase
    s = s.replace(" ", "").lower()
    
    # If palindrome rearrangement is not possible, return empty string
    if not can_form_palindrome(s):
        return ""
    
    # Count character frequencies
    char_counts = Counter(s)
    
    # Separate characters into those with even and odd frequencies
    even_chars = []
    odd_char = None
    
    for char, count in char_counts.items():
        if count % 2 == 0:
            even_chars.extend([char] * (count // 2))
        else:
            # If odd count, save the character for center
            if odd_char is None:
                odd_char = char
                even_chars.extend([char] * ((count - 1) // 2))
            else:
                even_chars.extend([char] * ((count - 1) // 2))
    
    # Construct palindrome
    left_half = ''.join(sorted(even_chars))
    right_half = left_half[::-1]
    
    # Add center character if exists
    middle = odd_char if odd_char else ''
    
    return left_half + middle + right_half