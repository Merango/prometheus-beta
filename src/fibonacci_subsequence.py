def generate_fibonacci_subsequence(n):
    """
    Generate a Fibonacci subsequence where the sum of even-indexed numbers equals n.
    
    Args:
        n (int): The target sum of even-indexed numbers in the subsequence.
    
    Returns:
        list: A Fibonacci subsequence where sum of even-indexed numbers is n.
        
    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special case: if n is 0, return [0]
    if n == 0:
        return [0]
    
    # Try to generate subsequence
    candidates = []
    
    # We'll use a breadth-first approach to find a valid subsequence
    def backtrack(current_sequence, target):
        # Base case: check if current sequence meets the condition
        even_sum = sum(current_sequence[::2])
        
        if even_sum == target:
            return current_sequence
        
        # If we've exceeded the target, backtrack
        if even_sum > target:
            return None
        
        # Try extending the sequence
        last_num = current_sequence[-1] if current_sequence else 0
        second_last_num = current_sequence[-2] if len(current_sequence) > 1 else 0
        
        next_num = last_num + second_last_num if len(current_sequence) > 1 else 1
        
        new_sequence = current_sequence + [next_num]
        
        result = backtrack(new_sequence, target)
        if result:
            return result
        
        return None
    
    # Attempt to generate subsequence
    result = backtrack([], n)
    
    if result is None:
        # If no subsequence found, raise an exception
        raise ValueError(f"No Fibonacci subsequence found with even-indexed sum of {n}")
    
    return result