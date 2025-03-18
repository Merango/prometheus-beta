from functools import wraps
from collections import defaultdict

class FunctionCallLogger:
    """
    A utility class to track and log the number of times functions are called.
    
    This class provides a decorator and methods to monitor function invocations.
    """
    
    _call_counts = defaultdict(int)
    
    @classmethod
    def log_calls(cls, func):
        """
        A decorator that logs the number of times a function is called.
        
        Args:
            func (callable): The function to be wrapped and tracked.
        
        Returns:
            callable: A wrapped function that tracks its own call count.
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Increment the call count for this specific function
            cls._call_counts[func.__name__] += 1
            # Call the original function
            return func(*args, **kwargs)
        return wrapper
    
    @classmethod
    def get_call_count(cls, func_name=None):
        """
        Retrieve the number of times a function (or all functions) has been called.
        
        Args:
            func_name (str, optional): Name of the specific function to check. 
                                       If None, returns a dictionary of all function call counts.
        
        Returns:
            int or dict: Call count for a specific function or dictionary of all call counts.
        """
        if func_name is None:
            return dict(cls._call_counts)
        
        return cls._call_counts[func_name]
    
    @classmethod
    def reset_call_counts(cls):
        """
        Reset the call counts for all tracked functions.
        """
        cls._call_counts.clear()