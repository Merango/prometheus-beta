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
    if n == 1:
        return [0, 1, 1]
    if n == 2:
        return [1, 1, 2]
    
    # Track all possible solutions
    def find_subsequence(target):
        # Maximum number of iterations to prevent infinite recursion
        max_iterations = 100
        
        for length in range(3, max_iterations):
            # Initialize Fibonacci sequence
            fib = [0, 1, 1]
            
            # Extend Fibonacci sequence if needed
            while len(fib) < length:
                fib.append(fib[-1] + fib[-2])
            
            # Check if subsequence works
            if sum(fib[::2]) == target:
                return fib
        
        # If no subsequence found after many attempts
        raise ValueError(f"No Fibonacci subsequence found with even-indexed sum of {target}")
    
    # Attempt to generate subsequence
    return find_subsequence(n)