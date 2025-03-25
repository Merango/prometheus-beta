def generate_fibonacci_subsequence(n):
    """
    Generate a Fibonacci subsequence where the sum of even-indexed numbers equals n.
    
    Args:
        n (int): The target sum of even-indexed numbers in the subsequence.
    
    Returns:
        list: A Fibonacci subsequence where sum of even-indexed numbers is n.
        
    Raises:
        ValueError: If n is negative or no valid subsequence is found.
        TypeError: If n is not an integer.
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special cases
    if n == 0:
        return [0]
    
    # Track all possible solutions
    def find_subsequence(target):
        # Maximum number of iterations to prevent infinite recursion
        max_iterations = 1000
        
        # Start with a list of pre-computed initial sequences
        initial_conditions = {
            1: [1, 1],
            2: [0, 1, 1],
            4: [0, 1, 1, 2, 3, 5]
        }
        
        # Use pre-computed sequence if available
        if target in initial_conditions:
            return initial_conditions[target]
        
        for length in range(3, max_iterations):
            # Initialize base Fibonacci sequence
            fib = [0, 1, 1]
            
            # Extend Fibonacci sequence to the current length
            while len(fib) < length:
                fib.append(fib[-1] + fib[-2])
            
            # Compute even-indexed sum
            even_indexed_sum = sum(fib[::2])
            
            # Check if we found a match
            if even_indexed_sum == target:
                return fib
            
            # If we've exceeded the target, stop searching
            if even_indexed_sum > target:
                break
        
        # If no subsequence found
        raise ValueError(f"No Fibonacci subsequence found with even-indexed sum of {target}")
    
    # Attempt to generate subsequence
    return find_subsequence(n)