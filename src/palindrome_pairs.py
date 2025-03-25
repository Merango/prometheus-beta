def find_palindrome_pairs(words):
    """
    Find all pairs of indices in an array of strings where concatenated strings form a palindrome.
    
    Args:
        words (List[str]): A list of strings to check for palindrome pairs
    
    Returns:
        List[List[int]]: A list of index pairs where concatenated words form a palindrome
    
    Time Complexity: O(n^2 * k), where n is the number of words and k is the average word length
    Space Complexity: O(1) for result, not counting the output space
    """
    def is_palindrome(s):
        """Check if a string is a palindrome."""
        return s == s[::-1]
    
    result = []
    n = len(words)
    
    for i in range(n):
        for j in range(n):
            if i != j:
                # Check if concatenating words in both orders forms a palindrome
                concat1 = words[i] + words[j]
                concat2 = words[j] + words[i]
                
                if is_palindrome(concat1):
                    result.append([i, j])
                # Avoid duplicate pairs, check second concatenation separately
                if is_palindrome(concat2) and [j, i] not in result:
                    result.append([j, i])
    
    return result