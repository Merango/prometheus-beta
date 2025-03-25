def filter_primes(numbers):
    """
    Filter out prime numbers from a given list of numbers.
    
    Args:
        numbers (list): A list of integers (positive and negative)
    
    Returns:
        list: A list of prime numbers from the input list
    
    Notes:
        - 0 and 1 are not considered prime numbers
        - Negative numbers are checked for primality by their absolute value
        - Negative primes are included in the result
    """
    def is_prime(n):
        # Handle special cases
        if n < 2:
            return False
        
        # Take absolute value for primality check
        abs_n = abs(n)
        
        # Check for primality of absolute value
        if abs_n == 2:
            return True
        
        # Even numbers > 2 are not prime
        if abs_n % 2 == 0:
            return False
        
        # Check odd divisors up to square root of absolute value
        for i in range(3, int(abs_n**0.5) + 1, 2):
            if abs_n % i == 0:
                return False
        
        return True
    
    # Return list of prime numbers, preserving sign
    return [num for num in numbers if is_prime(num)]