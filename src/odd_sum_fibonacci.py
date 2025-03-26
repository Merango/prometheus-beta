def generate_odd_sum_fibonacci(n):
    """
    Generate a modified Fibonacci sequence where consecutive term sums 
    are always odd.

    Args:
        n (int): The number of terms to generate in the sequence.

    Returns:
        list: A list of the first n numbers in the modified sequence.

    Raises:
        ValueError: If n is less than 0.
    """
    # Validate input
    if n < 0:
        raise ValueError("Number of terms must be non-negative")
    
    # Handle special cases for small n
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    # Initialize with the first few terms of the sequence
    sequence = [0, 1, 1, 2, 3]
    
    # Generate remaining terms
    while len(sequence) < n:
        # Calculate next term using Fibonacci-like addition
        next_term = sequence[-2] + sequence[-1]
        
        # Modify to ensure an odd sum between consecutive terms
        if (sequence[-1] + next_term) % 2 == 0:
            # If sum is even, adjust the term to make it odd
            next_term += 1
        
        sequence.append(next_term)
    
    return sequence[:n]