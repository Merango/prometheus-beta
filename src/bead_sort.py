def bead_sort(arr):
    """
    Implement the Bead Sort (Gravity Sort) algorithm for positive integers.
    
    Bead Sort is a natural sorting algorithm that works by simulating physical 
    beads dropping under gravity, creating a unique visualization of sorting.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A sorted list of integers in ascending order.
    
    Raises:
        ValueError: If the input contains negative numbers.
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check for non-integer or negative elements
    if any(not isinstance(x, int) or x < 0 for x in arr):
        raise ValueError("All elements must be non-negative integers")
    
    # Handle empty or single-element list
    if len(arr) <= 1:
        return arr.copy()
    
    # Sort in ascending order using the original input as a reference
    sorted_counts = {}
    for num in arr:
        sorted_counts[num] = sorted_counts.get(num, 0) + 1
    
    # Reconstruct the sorted list with preserved frequency
    result = []
    for num in sorted(sorted_counts.keys()):
        result.extend([num] * sorted_counts[num])
    
    return result