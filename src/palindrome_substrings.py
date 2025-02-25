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
    
    # Find non-overlapping palindromic substrings
    palindromes = set()
    n = len(s)
    
    for length in range(n, 1, -1):
        found = set()
        i = 0
        while i < n:
            # Look for palindrome of current length
            if i + length <= n:
                substr = s[i:i+length]
                if is_palindrome(substr):
                    # Only add if no previous palindrome overlaps
                    if not any(substr in p for p in found):
                        found.add(substr)
                        # Skip past this palindrome to ensure non-overlapping
                        i += length
                        continue
            i += 1
        
        # Add found palindromes to main set
        palindromes.update(found)
    
    # Sort and return unique palindromes
    return sorted(list(palindromes), key=lambda x: (len(x), x))