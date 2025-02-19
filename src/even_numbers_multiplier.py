def multiply_even_numbers(numbers):
    """
    Takes an array of numbers and returns a new array with even numbers multiplied by 2.
    
    Args:
        numbers (list): A list of numbers
    
    Returns:
        list: A new list where even numbers are multiplied by 2, odd numbers remain unchanged
    """
    return [num * 2 if num % 2 == 0 else num for num in numbers]