def find_non_overlapping_palindromes(s: str) -> list:
    """
    Find all non-overlapping palindromic substrings in the input string.
    
    Args:
        s (str): Input string to find palindromic substrings
    
    Returns:
        list: Sorted list of unique non-overlapping palindromic substrings
    
    Raises:
        TypeError: If input is not a string
    """
    # Check input type
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # If string is empty or too short, return empty list
    if len(s) < 2:
        return []
    
    # Function to check if a substring is a palindrome
    def is_palindrome(substr):
        return substr == substr[::-1]
    
    # Find all palindromic substrings
    palindromes = set()
    n = len(s)
    
    # Iterate through all possible substrings
    for i in range(n):
        for j in range(i+1, n+1):
            substr = s[i:j]
            if is_palindrome(substr) and len(substr) > 1:
                palindromes.add(substr)
    
    # Sort and return unique palindromes
    return sorted(list(palindromes))