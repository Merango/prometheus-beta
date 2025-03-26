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
    
    # Separate characters for palindrome construction
    even_chars = []
    center_chars = []
    
    for char, count in sorted(char_counts.items()):
        # Divide characters into pairs and keep any single character
        if count % 2 == 0:
            even_chars.extend([char] * (count // 2))
        else:
            center_chars.append(char)
            even_chars.extend([char] * ((count - 1) // 2))
    
    # Sort even chars to ensure consistent output
    even_chars.sort()
    
    # Construct palindrome
    left_half = ''.join(even_chars)
    right_half = left_half[::-1]
    
    # Add center character if exists (for odd length palindromes)
    middle = ''.join(center_chars)
    
    return left_half + middle + right_half