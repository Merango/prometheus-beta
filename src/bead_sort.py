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
    
    # Find the maximum element to determine the number of beads
    max_val = max(arr)
    
    # Create a 2D list representing beads (abacus-like representation)
    # where each row represents a set of beads for an element
    beads = [[1 if x > j else 0 for x in arr] for j in range(max_val)]
    
    # Collect beads from the bottom row (gravity simulation)
    sorted_arr = []
    for j in range(max_val):
        # Count number of beads in this row
        col_count = sum(row[j] for row in beads)
        
        # Add the indices where beads drop
        sorted_arr.extend([1] * col_count)
    
    return sorted_arr