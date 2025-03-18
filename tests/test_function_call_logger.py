import pytest
from src.function_call_logger import FunctionCallLogger

class TestFunctionCallLogger:
    def setup_method(self):
        # Reset call counts before each test
        FunctionCallLogger.reset_call_counts()
    
    def test_basic_call_counting(self):
        @FunctionCallLogger.log_calls
        def test_func():
            return "Hello"
        
        # Call the function multiple times
        test_func()
        test_func()
        test_func()
        
        # Check the call count
        assert FunctionCallLogger.get_call_count('test_func') == 3
    
    def test_multiple_functions(self):
        @FunctionCallLogger.log_calls
        def func1():
            return "Func1"
        
        @FunctionCallLogger.log_calls
        def func2():
            return "Func2"
        
        func1()
        func1()
        func2()
        
        assert FunctionCallLogger.get_call_count('func1') == 2
        assert FunctionCallLogger.get_call_count('func2') == 1
    
    def test_get_all_call_counts(self):
        @FunctionCallLogger.log_calls
        def func_a():
            pass
        
        @FunctionCallLogger.log_calls
        def func_b():
            pass
        
        func_a()
        func_a()
        func_b()
        
        counts = FunctionCallLogger.get_call_count()
        assert counts == {'func_a': 2, 'func_b': 1}
    
    def test_reset_call_counts(self):
        @FunctionCallLogger.log_calls
        def test_reset_func():
            pass
        
        test_reset_func()
        test_reset_func()
        
        assert FunctionCallLogger.get_call_count('test_reset_func') == 2
        
        FunctionCallLogger.reset_call_counts()
        
        assert FunctionCallLogger.get_call_count('test_reset_func') == 0
    
    def test_function_with_args(self):
        @FunctionCallLogger.log_calls
        def func_with_args(x, y):
            return x + y
        
        func_with_args(1, 2)
        func_with_args(3, 4)
        
        assert FunctionCallLogger.get_call_count('func_with_args') == 2
    
    def test_decorator_preserves_function_metadata(self):
        @FunctionCallLogger.log_calls
        def documented_func():
            """This is a documented function."""
            pass
        
        assert documented_func.__name__ == 'documented_func'
        assert documented_func.__doc__ == 'This is a documented function.'