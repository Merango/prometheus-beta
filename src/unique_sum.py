def sum_unique_elements(arr):
    """
    Calculate the sum of unique elements in the given array.
    
    Args:
        arr (list): A list of integers to process.
    
    Returns:
        int: The sum of unique elements in the array.
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    # Use a dictionary to track element counts
    element_counts = {}
    
    # Count occurrences of each element
    for num in arr:
        element_counts[num] = element_counts.get(num, 0) + 1
    
    # Calculate sum of unique elements (those with exactly one occurrence)
    unique_sum = sum(num for num, count in element_counts.items() if count == 1)
    
    return unique_sum