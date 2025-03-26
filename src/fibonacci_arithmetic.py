def find_fibonacci_arithmetic_progression(n):
    """
    Find the first n Fibonacci numbers that form an arithmetic progression.
    
    An arithmetic progression is a sequence where the difference between 
    consecutive terms is constant.
    
    Args:
        n (int): The number of Fibonacci numbers to find in the arithmetic progression.
    
    Returns:
        list: A list of n Fibonacci numbers forming an arithmetic progression.
    
    Raises:
        ValueError: If n is less than 1.
        ValueError: If no arithmetic progression of Fibonacci numbers is found.
    """
    # Validate input
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    
    # Start with the first few Fibonacci numbers
    fib = [0, 1]
    
    # Keep track of the longest arithmetic progression
    best_progression = []
    
    # Try all possible start indices and lengths
    for start in range(len(fib)):
        for length in range(3, n + 1):  # We need at least 3 numbers to form an arithmetic progression
            # Extend Fibonacci sequence if needed
            while len(fib) < start + length:
                fib.append(fib[-1] + fib[-2])
            
            # Check if the subsequence is an arithmetic progression
            subsequence = fib[start:start+length]
            differences = [subsequence[i+1] - subsequence[i] for i in range(length-1)]
            
            # If all differences are the same, we've found an arithmetic progression
            if len(set(differences)) == 1:
                if length > len(best_progression):
                    best_progression = subsequence
    
    # If no progression found or progression is shorter than requested
    if len(best_progression) < n:
        raise ValueError(f"Could not find an arithmetic progression of {n} Fibonacci numbers")
    
    return best_progression[:n]