def remove_duplicates(arr):
    """
    Remove duplicate elements from an input array while preserving the original order.
    
    Args:
        arr (list): Input list of integers
    
    Returns:
        list: A new list with duplicates removed, maintaining the order of first occurrence
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    Examples:
        >>> remove_duplicates([1, 2, 3, 2, 4, 1, 5])
        [1, 2, 3, 4, 5]
        >>> remove_duplicates([])
        []
        >>> remove_duplicates([1, 1, 1, 1])
        [1]
    """
    # Use a set to track seen elements for O(1) lookup
    seen = set()
    # Use a list comprehension to preserve order and remove duplicates
    return [x for x in arr if not (x in seen or seen.add(x))]