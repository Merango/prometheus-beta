import os
import pytest
from src.file_reader import read_file_lines

def test_read_file_lines_basic():
    """Test reading a standard text file."""
    # Create a temporary test file
    test_file_path = 'tests/test_file.txt'
    with open(test_file_path, 'w') as f:
        f.write("Hello\nWorld\nPython")
    
    try:
        # Read the file
        lines = read_file_lines(test_file_path)
        
        # Check the contents
        assert lines == ['Hello', 'World', 'Python']
        assert len(lines) == 3
    finally:
        # Clean up the test file
        os.remove(test_file_path)

def test_empty_file():
    """Test reading an empty file."""
    # Create an empty test file
    test_file_path = 'tests/empty_file.txt'
    with open(test_file_path, 'w') as f:
        pass
    
    try:
        # Read the empty file
        lines = read_file_lines(test_file_path)
        
        # Check that it returns an empty list
        assert lines == []
    finally:
        # Clean up the test file
        os.remove(test_file_path)

def test_file_not_found():
    """Test handling of non-existent file."""
    with pytest.raises(FileNotFoundError, match="The file 'nonexistent.txt' was not found."):
        read_file_lines('nonexistent.txt')

def test_file_with_newlines():
    """Test file with multiple newlines and empty lines."""
    # Create a test file with various newline scenarios
    test_file_path = 'tests/newline_test.txt'
    with open(test_file_path, 'w') as f:
        f.write("Line 1\n\nLine 3\n\n\nLine 6")
    
    try:
        # Read the file
        lines = read_file_lines(test_file_path)
        
        # Check the contents, noting that splitlines() removes empty lines
        assert lines == ['Line 1', '', 'Line 3', '', '', 'Line 6']
        assert len(lines) == 6
    finally:
        # Clean up the test file
        os.remove(test_file_path)