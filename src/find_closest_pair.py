def find_closest_pair(numbers):
    """
    Find the closest pair of numbers in the given array.
    
    Args:
        numbers (list): A list of numbers to search through.
    
    Returns:
        tuple: A tuple containing two numbers that are closest to each other.
               In case of a tie, returns the pair with the smallest numbers.
    
    Raises:
        ValueError: If the input list has fewer than 2 numbers.
    """
    # Check for invalid input
    if not numbers or len(numbers) < 2:
        raise ValueError("Input list must contain at least two numbers")
    
    # Sort the input list to help with finding the closest pair
    sorted_nums = sorted(numbers)
    
    # Initialize variables to track the closest pair
    min_diff = float('inf')
    closest_pair = None
    
    # Compare all pairs of numbers to handle any combination
    for i in range(len(sorted_nums)):
        for j in range(i+1, len(sorted_nums)):
            current_diff = abs(sorted_nums[i] - sorted_nums[j])
            
            # Update closest pair if current difference is smaller
            if current_diff < min_diff:
                min_diff = current_diff
                closest_pair = (sorted_nums[i], sorted_nums[j])
            # If differences are equal, choose the pair with smaller numbers
            elif current_diff == min_diff:
                candidate_pair = (sorted_nums[i], sorted_nums[j])
                # Compare pairs lexicographically
                closest_pair = min(closest_pair, candidate_pair)
    
    return closest_pair