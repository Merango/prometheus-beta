import os
import pytest
import tempfile
import shutil

from src.directory_files import list_directory_files

def test_list_directory_files_empty_directory():
    """Test listing files in an empty directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        assert list_directory_files(temp_dir) == []

def test_list_directory_files_with_files():
    """Test listing files in a directory with multiple files."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test files
        test_files = ['file1.txt', 'file2.txt', 'file3.py']
        for filename in test_files:
            with open(os.path.join(temp_dir, filename), 'w') as f:
                f.write('test content')
        
        # Create a subdirectory to ensure it's not included
        os.mkdir(os.path.join(temp_dir, 'subdir'))
        
        # Check if only files are returned
        result = list_directory_files(temp_dir)
        assert set(result) == set(test_files)

def test_list_directory_files_nonexistent_directory():
    """Test that FileNotFoundError is raised for nonexistent directory."""
    with pytest.raises(FileNotFoundError):
        list_directory_files('/path/to/nonexistent/directory')

def test_list_directory_files_not_a_directory():
    """Test that NotADirectoryError is raised when path is not a directory."""
    with tempfile.NamedTemporaryFile() as temp_file:
        with pytest.raises(NotADirectoryError):
            list_directory_files(temp_file.name)

def test_list_directory_files_with_special_characters():
    """Test listing files with special characters in filenames."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create files with special characters
        test_files = ['file with spaces.txt', 'file@special.py', 'file#hash.txt']
        for filename in test_files:
            with open(os.path.join(temp_dir, filename), 'w') as f:
                f.write('test content')
        
        result = list_directory_files(temp_dir)
        assert set(result) == set(test_files)