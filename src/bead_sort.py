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
    
    # Create a 2D representation of beads
    beads = [[1 if x > j else 0 for x in arr] for j in range(max_val)]
    
    # Let the beads "drop"
    for j in range(max_val):
        # Count beads in each column
        col_sum = sum(row[j] for row in beads)
        
        # Rearrange beads from bottom
        for i in range(len(arr)):
            beads[j][i] = 1 if i < col_sum else 0
    
    # Reconstruct the sorted array
    sorted_arr = [sum(row[i] for row in beads) for i in range(len(arr))]
    
    return sorted_arr