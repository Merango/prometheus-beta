import os
import pytest
import tempfile
import shutil

from src.file_creator import create_text_file

def test_create_empty_file():
    """Test creating an empty file."""
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, 'empty_file.txt')
        assert create_text_file(file_path) is True
        assert os.path.exists(file_path)
        assert os.path.getsize(file_path) == 0

def test_create_file_with_content():
    """Test creating a file with specific content."""
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = os.path.join(tmpdir, 'file_with_content.txt')
        test_content = "Hello, World!"
        assert create_text_file(file_path, test_content) is True
        
        with open(file_path, 'r') as f:
            assert f.read() == test_content

def test_create_file_in_nested_directory():
    """Test creating a file in a nested directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        nested_path = os.path.join(tmpdir, 'nested', 'dir', 'file.txt')
        assert create_text_file(nested_path) is True
        assert os.path.exists(nested_path)

def test_empty_file_path_raises_error():
    """Test that empty file path raises ValueError."""
    with pytest.raises(ValueError):
        create_text_file('')
    
    with pytest.raises(ValueError):
        create_text_file(None)