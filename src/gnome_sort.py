def gnome_sort(arr):
    """
    Implement the Gnome Sort (Stupid Sort) algorithm.
    
    Gnome Sort is a simple sorting algorithm that works similar to how a gardener 
    sorts plants. It compares adjacent elements and swaps them if they are in the 
    wrong order, moving back and forth through the array.
    
    Args:
        arr (list): The input list to be sorted.
    
    Returns:
        list: A new sorted list in ascending order.
    
    Raises:
        TypeError: If the input is not a list or contains unsortable elements.
    """
    # Create a copy to avoid modifying the original list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr.copy()
    
    # Create a mutable copy to work with
    sorted_arr = arr.copy()
    
    # Start from the second element (index 1)
    i = 1
    while i < len(sorted_arr):
        # If current element is smaller than the previous one, swap and move back
        if i > 0 and sorted_arr[i] < sorted_arr[i-1]:
            sorted_arr[i], sorted_arr[i-1] = sorted_arr[i-1], sorted_arr[i]
            i -= 1
        else:
            # Move forward if elements are in correct order
            i += 1
    
    return sorted_arr