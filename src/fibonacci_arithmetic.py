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
    
    # If n is less than 3, just return Fibonacci numbers
    if n <= 2:
        return (lambda fib: fib[:n])([0, 1])
    
    # Start with the first few Fibonacci numbers
    fib = [0, 1]
    
    # Extend Fibonacci sequence to have enough numbers
    while len(fib) < 20:  # Increased search space
        fib.append(fib[-1] + fib[-2])
    
    # Try different subsequences
    for start in range(len(fib) - n + 1):
        subsequence = fib[start:start+n]
        
        # Check for arithmetic progression
        differences = [subsequence[i+1] - subsequence[i] for i in range(n-1)]
        if len(set(differences)) == 1:
            return subsequence
    
    # If no progression found
    raise ValueError(f"Could not find an arithmetic progression of {n} Fibonacci numbers")