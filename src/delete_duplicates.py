def deleteDuplicates(arr):
    """
    Remove duplicate elements from an array while preserving the original order.

    Args:
        arr (list): Input list of integers with potential duplicates.

    Returns:
        list: A new list with duplicates removed, maintaining the original order.

    Examples:
        >>> deleteDuplicates([1, 2, 3, 2, 1, 5, 6, 5, 5, 7])
        [1, 2, 3, 5, 6, 7]
        >>> deleteDuplicates([])
        []
        >>> deleteDuplicates([1, 1, 1, 1])
        [1]
    """
    # Use a set to track seen elements while preserving order
    seen = set()
    result = []
    
    for item in arr:
        # Only add to result if not seen before
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result