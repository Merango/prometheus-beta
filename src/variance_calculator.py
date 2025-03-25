def calculate_variance(numbers):
    """
    Calculate the variance of a list of numbers.

    Variance is a measure of variability calculated as the average of squared 
    deviations from the mean. For a sample, this uses the sample variance formula.

    Args:
        numbers (list): A list of numeric values.

    Returns:
        float: The variance of the input list.

    Raises:
        TypeError: If the input is not a list or contains non-numeric values.
        ValueError: If the list is empty.
    """
    # Validate input
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    # Check for empty list
    if len(numbers) == 0:
        raise ValueError("Cannot calculate variance of an empty list")
    
    # Validate all elements are numeric
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All elements must be numeric")
    
    # Calculate mean
    mean = sum(numbers) / len(numbers)
    
    # Calculate variance (sample variance)
    squared_deviations = [(x - mean) ** 2 for x in numbers]
    variance = sum(squared_deviations) / (len(numbers) - 1)
    
    return variance