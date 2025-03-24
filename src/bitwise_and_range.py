def bitwise_and_range(start: int, end: int) -> int:
    """
    Calculate the bitwise AND of all numbers in the given range (inclusive).

    This function performs a bitwise AND operation on all numbers from start to end.
    It efficiently handles the calculation by finding the common prefix of binary 
    representations.

    Args:
        start (int): The start of the range (inclusive)
        end (int): The end of the range (inclusive)

    Returns:
        int: The result of bitwise AND operation on all numbers in the range

    Raises:
        ValueError: If start is greater than end or if either number is negative
    """
    # Validate input
    if start < 0 or end < 0:
        raise ValueError("Both start and end must be non-negative integers")
    
    if start > end:
        raise ValueError("Start must be less than or equal to end")
    
    # If start and end are the same, return the number itself
    if start == end:
        return start
    
    # Count the number of shifts needed to find common prefix
    shift = 0
    while start != end:
        start >>= 1
        end >>= 1
        shift += 1
    
    # Shift back to get the common prefix
    return start << shift