import pytest
import sys
from io import StringIO
from src.log_bold import log_bold

def test_log_bold_basic():
    """Test basic logging of a bold message."""
    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # Call the function
    result = log_bold("Hello, World!")
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Check the result
    assert result == "\033[1mHello, World!\033[0m"
    assert captured_output.getvalue().strip() == "\033[1mHello, World!\033[0m"

def test_log_bold_empty_string():
    """Test that an empty string raises a ValueError."""
    with pytest.raises(ValueError, match="Message cannot be empty"):
        log_bold("")

def test_log_bold_non_string():
    """Test that non-string inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be a string"):
        log_bold(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        log_bold(None)

def test_log_bold_special_characters():
    """Test logging messages with special characters."""
    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # Call the function
    result = log_bold("Hello, @#$%^&*()!")
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Check the result
    assert result == "\033[1mHello, @#$%^&*()!\033[0m"
    assert captured_output.getvalue().strip() == "\033[1mHello, @#$%^&*()!\033[0m"