def bitonic_sort(arr, ascending=True):
    """
    Implement the Bitonic Sort algorithm.
    
    Bitonic sort is a comparison-based sorting algorithm that can be run in parallel.
    It works by first creating a bitonic sequence and then merging it.
    
    Args:
        arr (list): The input list to be sorted
        ascending (bool, optional): Sort in ascending order if True, 
                                    descending order if False. Defaults to True.
    
    Returns:
        list: A new sorted list
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains elements that cannot be compared
    """
    # Create a copy to avoid modifying the original list
    def compare_and_swap(arr, i, j, direction):
        """
        Compare and swap elements if they are in the wrong order.
        
        Args:
            arr (list): The list to modify
            i (int): First index to compare
            j (int): Second index to compare
            direction (bool): True for ascending, False for descending
        """
        if (direction and arr[i] > arr[j]) or (not direction and arr[i] < arr[j]):
            arr[i], arr[j] = arr[j], arr[i]
    
    def bitonic_merge(arr, low, count, direction):
        """
        Merge a bitonic sequence.
        
        Args:
            arr (list): The list to merge
            low (int): Starting index of the sequence
            count (int): Number of elements to merge
            direction (bool): True for ascending, False for descending
        """
        if count > 1:
            k = count // 2
            for i in range(low, low + k):
                compare_and_swap(arr, i, i + k, direction)
            
            bitonic_merge(arr, low, k, direction)
            bitonic_merge(arr, low + k, k, direction)
    
    def bitonic_sort_recursive(arr, low, count, direction):
        """
        Recursively sort a bitonic sequence.
        
        Args:
            arr (list): The list to sort
            low (int): Starting index of the sequence
            count (int): Number of elements to sort
            direction (bool): True for ascending, False for descending
        """
        if count > 1:
            k = count // 2
            
            # Sort first half in ascending order
            bitonic_sort_recursive(arr, low, k, True)
            
            # Sort second half in descending order
            bitonic_sort_recursive(arr, low + k, k, False)
            
            # Merge the entire sequence
            bitonic_merge(arr, low, count, direction)
    
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Create a copy of the input list
    sorted_arr = arr.copy()
    
    # If the list is empty or has only one element, return it
    if len(sorted_arr) <= 1:
        return sorted_arr
    
    # Find the next power of 2 larger than or equal to the list length
    n = len(sorted_arr)
    next_power_of_2 = 1
    while next_power_of_2 < n:
        next_power_of_2 *= 2
    
    # Pad the list with the last element to make it a power of 2
    while len(sorted_arr) < next_power_of_2:
        sorted_arr.append(sorted_arr[-1])
    
    # Perform bitonic sort
    bitonic_sort_recursive(sorted_arr, 0, len(sorted_arr), ascending)
    
    # Return the list trimmed to original length
    return sorted_arr[:n]