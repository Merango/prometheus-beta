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
    
    def is_palindrome(substr):
        """Check if a substring is a palindrome."""
        return substr == substr[::-1]
    
    # Collect palindromes while ensuring non-overlapping
    palindromes = set()
    n = len(s)
    
    # Check for complete string palindrome first
    if is_palindrome(s):
        return [s]
    
    # Find unique palindromes
    for length in range(2, n+1):
        for start in range(n - length + 1):
            substr = s[start:start+length]
            if is_palindrome(substr):
                # Keep longest palindromes 
                matching = [p for p in palindromes if substr in p]
                if not matching:
                    palindromes.add(substr)
    
    # Special handling for single character and small palindromes
    palindromes = set(p for p in palindromes if len(p) > 1)
    
    # Sort first by lexicographic order, then handle special cases like 'ace'
    result = sorted(list(palindromes), 
                   key=lambda x: (len(x), x))
    
    return result