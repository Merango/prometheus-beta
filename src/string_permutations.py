def generate_unique_permutations(s: str) -> list[str]:
    """
    Generate all unique permutations of a given string.
    
    This function finds all unique arrangements of characters in the input string,
    eliminating duplicate permutations.
    
    Args:
        s (str): The input string to generate permutations for.
    
    Returns:
        list[str]: A list of unique permutations of the input string.
    
    Examples:
        >>> generate_unique_permutations('abc')
        ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
        >>> generate_unique_permutations('aba')
        ['aba', 'aab', 'baa']
    
    Raises:
        TypeError: If input is not a string.
    """
    # Validate input
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if not s:
        return []
    
    # Use a set to store unique permutations
    unique_perms = set()
    
    def backtrack(current_perm, remaining_chars):
        # Base case: if no characters left, add the permutation
        if not remaining_chars:
            unique_perms.add(current_perm)
            return
        
        # Try each remaining character as the next in the permutation
        for i in range(len(remaining_chars)):
            # Choose a character
            next_char = remaining_chars[i]
            
            # Create new strings for recursive call
            new_perm = current_perm + next_char
            new_remaining = remaining_chars[:i] + remaining_chars[i+1:]
            
            # Recursive backtracking
            backtrack(new_perm, new_remaining)
    
    # Start the backtracking process
    backtrack('', s)
    
    # Convert set to sorted list for consistent output
    return sorted(list(unique_perms))