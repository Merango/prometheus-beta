def generate_odd_sum_fibonacci(n):
    """
    Generate a Fibonacci-like sequence where the sum of any two consecutive 
    numbers is always odd.

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
    
    # Initialize the sequence
    sequence = [0, 1, 1, 2, 3]
    
    # Generate subsequent terms
    while len(sequence) < n:
        # Ensure the sum is always odd by carefully selecting the next term
        next_term = sequence[-1] + sequence[-2]
        
        # If the sum is even, add 1 to make it odd
        if (sequence[-1] + next_term) % 2 == 0:
            next_term += 1
        
        sequence.append(next_term)
    
    return sequence[:n]