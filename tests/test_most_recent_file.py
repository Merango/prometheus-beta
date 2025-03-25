import os
import pytest
import tempfile
import time
from src.most_recent_file import find_most_recent_file

def test_find_most_recent_file():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create some test files with different modification times
        file1_path = os.path.join(temp_dir, 'file1.txt')
        file2_path = os.path.join(temp_dir, 'file2.txt')
        file3_path = os.path.join(temp_dir, 'file3.txt')
        
        # Create files and stagger their modification times
        with open(file1_path, 'w') as f:
            f.write('content1')
        time.sleep(0.1)  # Ensure different modification times
        
        with open(file2_path, 'w') as f:
            f.write('content2')
        time.sleep(0.1)
        
        with open(file3_path, 'w') as f:
            f.write('content3')
        
        # Find the most recently modified file
        most_recent = find_most_recent_file(temp_dir)
        
        # Verify it's the last created file
        assert most_recent == file3_path

def test_empty_directory():
    # Create an empty temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Should return None for an empty directory
        assert find_most_recent_file(temp_dir) is None

def test_non_existent_directory():
    # Should return None for a non-existent directory
    assert find_most_recent_file('/path/to/non/existent/directory') is None

def test_not_a_directory():
    # Create a temporary file
    with tempfile.NamedTemporaryFile() as temp_file:
        # Should raise NotADirectoryError
        with pytest.raises(NotADirectoryError):
            find_most_recent_file(temp_file.name)

def test_no_read_permissions():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Remove read permissions
        os.chmod(temp_dir, 0o000)
        
        # Should raise PermissionError
        with pytest.raises(PermissionError):
            find_most_recent_file(temp_dir)
        
        # Restore permissions
        os.chmod(temp_dir, 0o755)