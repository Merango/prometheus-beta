def longest_common_subsequence(str1: str, str2: str) -> str:
    """
    Find the longest common subsequence between two input strings.
    
    A subsequence is a sequence that can be derived from another sequence 
    by deleting some or no elements without changing the order of the remaining elements.
    
    Args:
        str1 (str): First input string
        str2 (str): Second input string
    
    Returns:
        str: The longest common subsequence
    
    Raises:
        TypeError: If inputs are not strings
    """
    # Type checking
    if not (isinstance(str1, str) and isinstance(str2, str)):
        raise TypeError("Inputs must be strings")
    
    # Handle empty string cases
    if not str1 or not str2:
        return ""
    
    # Create a matrix to store LCS lengths
    m, n = len(str1), len(str2)
    # Add 1 to dimensions to account for empty string case
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                # If characters match, extend previous diagonal value
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                # If characters don't match, take max of previous results
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Reconstruct the longest common subsequence
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            # If characters match, add to LCS and move diagonally
            lcs.append(str1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            # Move up in the matrix
            i -= 1
        else:
            # Move left in the matrix
            j -= 1
    
    # Reverse to get correct order and convert to string
    return ''.join(reversed(lcs))