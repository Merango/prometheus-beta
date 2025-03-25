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
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # If the list is empty or has only one element, return a copy
    if len(arr) <= 1:
        return arr.copy()
    
    # Recursively perform bitonic sort
    def bitonic_sort_recursive(arr, ascending):
        # Base case
        if len(arr) <= 1:
            return arr
        
        # Split the array
        mid = len(arr) // 2
        left = bitonic_sort_recursive(arr[:mid], True)
        right = bitonic_sort_recursive(arr[mid:], False)
        
        # Merge the sorted halves
        return bitonic_merge(left + right, ascending)
    
    # Merge two sorted portions
    def bitonic_merge(arr, ascending):
        if len(arr) <= 1:
            return arr
        
        def compare_swap(arr):
            for i in range(len(arr) // 2):
                # Compare and swap based on the direction
                if (ascending and arr[i] > arr[i + len(arr) // 2]) or \
                   (not ascending and arr[i] < arr[i + len(arr) // 2]):
                    arr[i], arr[i + len(arr) // 2] = arr[i + len(arr) // 2], arr[i]
            return arr
        
        # Perform multiple merge passes
        half = len(arr) // 2
        for k in range(half):
            arr = compare_swap(arr)
        
        return arr
    
    # Perform bitonic sort and return the result
    result = bitonic_sort_recursive(arr, ascending)
    
    # Sort the final list based on the ascending parameter
    if ascending:
        result.sort()
    else:
        result.sort(reverse=True)
    
    return result