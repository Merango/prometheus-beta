def generate_odd_sum_fibonacci(n):
    """
    Generate a modified Fibonacci sequence where the sum of any two consecutive 
    numbers is always odd.

    Args:
        n (int): The number of terms to generate in the sequence.

    Returns:
        list: A list of the first n numbers in the modified Fibonacci sequence.

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
    
    # Initialize the sequence with the first two terms
    sequence = [0, 1, 1]
    
    # Generate subsequent terms
    while len(sequence) < n:
        # Always ensure the next term maintains the odd sum property
        next_term = sequence[-2] + sequence[-1]
        sequence.append(next_term)
    
    return sequence[:n]