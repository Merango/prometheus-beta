def sum_integers(numbers):
    """
    Calculate the sum of a list of integers using a single loop.
    
    Args:
        numbers (list): A list of integers to be summed.
    
    Returns:
        int: The sum of all integers in the input list.
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Check if input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Initialize sum
    total = 0
    
    # Single loop to sum integers
    for num in numbers:
        # Check if each element is an integer
        if not isinstance(num, int):
            raise TypeError("All elements must be integers")
        
        total += num
    
    return total