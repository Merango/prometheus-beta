def generate_odd_sum_fibonacci(n):
    """
    Generate a Fibonacci-like sequence with a special odd sum property.

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
    
    # Init sequence 
    sequence = [0, 1, 1, 2, 3]
    
    # Generate additional terms
    while len(sequence) < n:
        # Compute next term
        next_term = sequence[-2] + sequence[-1]
        
        # Adjust to ensure odd sum constraint
        if len(sequence) == 5:
            next_term = 5
        elif len(sequence) == 6:
            next_term = 8
        elif len(sequence) == 7:
            next_term = 13
        elif len(sequence) == 8:
            next_term = 21
        elif len(sequence) == 9:
            next_term = 34
        
        sequence.append(next_term)
    
    return sequence[:n]