import os
import shutil
import pytest
from src.directory_utils import create_directory

@pytest.fixture
def temp_dir():
    """Fixture to create and clean up a temporary test directory."""
    test_dir = 'test_temp_directory'
    yield test_dir
    # Cleanup: remove test directory if it exists
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)

def test_create_directory_success(temp_dir):
    """Test successful directory creation."""
    result = create_directory(temp_dir)
    assert result['success'] is True
    assert result['created'] is True
    assert os.path.isdir(temp_dir)

def test_create_directory_with_parents(temp_dir):
    """Test creating a nested directory with parents."""
    nested_dir = os.path.join(temp_dir, 'subdir', 'another')
    result = create_directory(nested_dir, parents=True)
    assert result['success'] is True
    assert result['created'] is True
    assert os.path.isdir(nested_dir)

def test_create_existing_directory_without_parents(temp_dir):
    """Test creating an existing directory without parents flag."""
    create_directory(temp_dir)
    result = create_directory(temp_dir)
    assert result['success'] is False
    assert result['created'] is False
    assert 'already exists' in result['error']

def test_create_directory_empty_path():
    """Test creating a directory with an empty path."""
    with pytest.raises(ValueError, match="Directory path cannot be None or empty"):
        create_directory("")

def test_create_directory_custom_mode(temp_dir):
    """Test creating a directory with custom mode."""
    result = create_directory(temp_dir, mode=0o700)
    assert result['success'] is True
    assert result['mode'] == 0o700
    assert os.path.isdir(temp_dir)
    # Optional: You might want to check actual permissions, but this varies by OS