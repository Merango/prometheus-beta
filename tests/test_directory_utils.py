import os
import pytest
import shutil
import tempfile

from src.directory_utils import delete_empty_directory

def test_delete_empty_directory():
    """Test deleting an empty directory successfully."""
    with tempfile.TemporaryDirectory() as base_dir:
        # Create an empty directory
        empty_dir = os.path.join(base_dir, 'empty_dir')
        os.makedirs(empty_dir)
        
        # Verify directory exists before deletion
        assert os.path.exists(empty_dir)
        
        # Delete the empty directory
        result = delete_empty_directory(empty_dir)
        
        # Verify deletion
        assert result is True
        assert not os.path.exists(empty_dir)

def test_delete_non_existent_directory():
    """Test attempting to delete a non-existent directory."""
    with tempfile.TemporaryDirectory() as base_dir:
        non_existent_path = os.path.join(base_dir, 'non_existent_dir')
        
        with pytest.raises(FileNotFoundError):
            delete_empty_directory(non_existent_path)

def test_delete_non_empty_directory():
    """Test attempting to delete a non-empty directory."""
    with tempfile.TemporaryDirectory() as base_dir:
        non_empty_dir = os.path.join(base_dir, 'non_empty_dir')
        os.makedirs(non_empty_dir)
        
        # Create a file inside the directory
        with open(os.path.join(non_empty_dir, 'file.txt'), 'w') as f:
            f.write('content')
        
        with pytest.raises(OSError, match="Directory is not empty"):
            delete_empty_directory(non_empty_dir)

def test_delete_file_not_directory():
    """Test attempting to delete a file instead of a directory."""
    with tempfile.TemporaryDirectory() as base_dir:
        file_path = os.path.join(base_dir, 'test_file.txt')
        with open(file_path, 'w') as f:
            f.write('content')
        
        with pytest.raises(ValueError, match="Path is not a directory"):
            delete_empty_directory(file_path)