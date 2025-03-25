import os
import tarfile
import pytest
import shutil
import tempfile

from src.tar_archiver import create_tar_archive


@pytest.fixture
def temp_source_dir():
    """Create a temporary directory with some test files."""
    temp_dir = tempfile.mkdtemp()
    try:
        # Create some test files
        with open(os.path.join(temp_dir, 'test1.txt'), 'w') as f:
            f.write('Test content 1')
        with open(os.path.join(temp_dir, 'test2.txt'), 'w') as f:
            f.write('Test content 2')
        
        # Create a subdirectory
        os.mkdir(os.path.join(temp_dir, 'subdir'))
        with open(os.path.join(temp_dir, 'subdir', 'test3.txt'), 'w') as f:
            f.write('Test content 3')
        
        yield temp_dir
    finally:
        # Clean up the temporary directory
        shutil.rmtree(temp_dir)


def test_create_tar_archive_default(temp_source_dir):
    """Test creating a tar.gz archive with default parameters."""
    archive_path = create_tar_archive(temp_source_dir)
    
    # Verify archive was created
    assert os.path.exists(archive_path)
    assert archive_path.endswith('.tar.gz')
    
    # Verify archive contents
    with tarfile.open(archive_path, 'r:gz') as tar:
        members = tar.getnames()
        assert len(members) > 0
        assert os.path.basename(temp_source_dir) in members


def test_create_tar_archive_custom_path(temp_source_dir):
    """Test creating a tar archive with a custom path."""
    custom_path = os.path.join(os.path.dirname(temp_source_dir), 'custom_archive.tar.gz')
    archive_path = create_tar_archive(temp_source_dir, custom_path)
    
    assert archive_path == custom_path
    assert os.path.exists(archive_path)


@pytest.mark.parametrize('compression', ['bz2', 'xz'])
def test_create_tar_archive_different_compression(temp_source_dir, compression):
    """Test creating tar archives with different compression types."""
    archive_path = create_tar_archive(temp_source_dir, compression=compression)
    
    assert os.path.exists(archive_path)
    assert archive_path.endswith(f'.tar.{compression}')
    
    # Verify archive can be opened
    with tarfile.open(archive_path, f'r:{compression}') as tar:
        members = tar.getnames()
        assert len(members) > 0


def test_create_tar_archive_nonexistent_dir():
    """Test that an error is raised for nonexistent directory."""
    with pytest.raises(ValueError, match="Source directory does not exist"):
        create_tar_archive('/path/to/nonexistent/directory')


def test_create_tar_archive_file_instead_of_dir():
    """Test that an error is raised when a file is passed instead of a directory."""
    with pytest.raises(ValueError, match="Source path is not a directory"):
        temp_file = tempfile.mktemp()
        try:
            with open(temp_file, 'w') as f:
                f.write('test')
            create_tar_archive(temp_file)
        finally:
            os.unlink(temp_file)


def test_create_tar_archive_invalid_compression():
    """Test that an error is raised for invalid compression type."""
    with pytest.raises(ValueError, match="Invalid compression type"):
        create_tar_archive(tempfile.mkdtemp(), compression='invalid')