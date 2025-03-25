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
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # If the list is empty or has only one element, return it
    if len(arr) <= 1:
        return arr.copy()
    
    def bitonic_merge(arr, start, length, direction):
        """
        Merge a bitonic sequence.
        
        Args:
            arr (list): The list to modify
            start (int): Starting index
            length (int): Length of sequence to merge
            direction (bool): True for ascending, False for descending
        """
        if length > 1:
            mid = length // 2
            for i in range(start, start + mid):
                if (direction and arr[i] > arr[i + mid]) or (not direction and arr[i] < arr[i + mid]):
                    arr[i], arr[i + mid] = arr[i + mid], arr[i]
            
            bitonic_merge(arr, start, mid, direction)
            bitonic_merge(arr, start + mid, mid, direction)
    
    def bitonic_sort_recursive(arr, start, length, direction):
        """
        Recursively sort a bitonic sequence.
        
        Args:
            arr (list): The list to modify
            start (int): Starting index
            length (int): Length of sequence to sort
            direction (bool): True for ascending, False for descending
        """
        if length > 1:
            mid = length // 2
            
            # Sort first half
            bitonic_sort_recursive(arr, start, mid, True)
            
            # Sort second half
            bitonic_sort_recursive(arr, start + mid, length - mid, False)
            
            # Merge the entire sequence
            bitonic_merge(arr, start, length, direction)
    
    # Create a copy of the input list
    sorted_arr = arr.copy()
    
    # Ensure the list size is a power of 2
    n = len(sorted_arr)
    next_power_of_2 = 1
    while next_power_of_2 < n:
        next_power_of_2 *= 2
    
    # Pad the list with the last element to make it a power of 2
    padded_arr = sorted_arr + [sorted_arr[-1]] * (next_power_of_2 - n)
    
    # Perform bitonic sort
    bitonic_sort_recursive(padded_arr, 0, next_power_of_2, ascending)
    
    # Return the list trimmed to original length
    return padded_arr[:n]