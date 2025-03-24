def find_first_last_occurrence(arr, target):
    """
    Find the first and last occurrence of a target element in a sorted array.
    
    Args:
        arr (list): A sorted list of elements 
        target: The element to find
    
    Returns:
        tuple: A tuple (first_index, last_index) where:
            - first_index is the index of the first occurrence of target
            - last_index is the index of the last occurrence of target
            - Returns (-1, -1) if the target is not found
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    def binary_search_first(arr, target):
        """Find the first occurrence of target"""
        left, right = 0, len(arr) - 1
        first_index = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == target:
                first_index = mid
                # Continue searching in the left half
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return first_index
    
    def binary_search_last(arr, target):
        """Find the last occurrence of target"""
        left, right = 0, len(arr) - 1
        last_index = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == target:
                last_index = mid
                # Continue searching in the right half
                left = mid + 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return last_index
    
    # Handle empty array case
    if not arr:
        return (-1, -1)
    
    # Find first and last occurrences
    first = binary_search_first(arr, target)
    
    # If target not found in first search, return (-1, -1)
    if first == -1:
        return (-1, -1)
    
    last = binary_search_last(arr, target)
    
    return (first, last)