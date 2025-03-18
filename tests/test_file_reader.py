"""
Test suite for file_reader module.
"""

import os
import pytest
import tempfile

from src.file_reader import read_file_contents

def test_read_existing_file():
    """Test reading contents of an existing file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write("Hello, world!")
        temp_file.close()
        
        try:
            content = read_file_contents(temp_file.name)
            assert content == "Hello, world!"
        finally:
            os.unlink(temp_file.name)

def test_read_empty_file():
    """Test reading an empty file."""
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.close()
        
        try:
            content = read_file_contents(temp_file.name)
            assert content == ""
        finally:
            os.unlink(temp_file.name)

def test_file_not_found():
    """Test handling of non-existent file."""
    with pytest.raises(FileNotFoundError):
        read_file_contents("non_existent_file.txt")

def test_invalid_input_types():
    """Test handling of invalid input types."""
    with pytest.raises(TypeError):
        read_file_contents(None)
    
    with pytest.raises(TypeError):
        read_file_contents(123)

def test_empty_path():
    """Test handling of empty file path."""
    with pytest.raises(ValueError):
        read_file_contents("")
    
    with pytest.raises(ValueError):
        read_file_contents("   ")

def test_directory_path():
    """Test handling of directory path."""
    with pytest.raises(IsADirectoryError):
        read_file_contents(".")

def test_unicode_file():
    """Test reading a file with unicode content."""
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False) as temp_file:
        temp_file.write("こんにちは世界")
        temp_file.close()
        
        try:
            content = read_file_contents(temp_file.name)
            assert content == "こんにちは世界"
        finally:
            os.unlink(temp_file.name)