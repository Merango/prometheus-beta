import os
import zipfile
import pytest
import tempfile
from src.zip_archiver import create_zip_archive

@pytest.fixture
def sample_files():
    """Create temporary sample files for testing."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create multiple sample files
        files = [
            os.path.join(tmpdir, 'file1.txt'),
            os.path.join(tmpdir, 'file2.txt')
        ]
        
        # Write some content to the files
        for file_path in files:
            with open(file_path, 'w') as f:
                f.write("Test content")
        
        yield files

def test_create_zip_archive_success(sample_files):
    """Test successful zip archive creation."""
    with tempfile.NamedTemporaryFile(suffix='.zip', delete=False) as temp_zip:
        temp_zip.close()
        
        # Create zip archive
        result = create_zip_archive(sample_files, temp_zip.name)
        
        # Verify successful creation
        assert result is True
        assert os.path.exists(temp_zip.name)
        
        # Verify contents of zip file
        with zipfile.ZipFile(temp_zip.name, 'r') as zf:
            assert len(zf.namelist()) == len(sample_files)
            for file in sample_files:
                assert os.path.basename(file) in zf.namelist()
        
        # Clean up
        os.unlink(temp_zip.name)

def test_create_zip_archive_empty_list():
    """Test handling of empty file list."""
    with tempfile.NamedTemporaryFile(suffix='.zip', delete=False) as temp_zip:
        temp_zip.close()
        
        # Verify ValueError is raised for empty file list
        with pytest.raises(ValueError, match="File list cannot be empty"):
            create_zip_archive([], temp_zip.name)
        
        # Clean up
        os.unlink(temp_zip.name)

def test_create_zip_archive_nonexistent_file():
    """Test handling of nonexistent files."""
    with tempfile.NamedTemporaryFile(suffix='.zip', delete=False) as temp_zip:
        temp_zip.close()
        
        # Verify FileNotFoundError is raised for nonexistent file
        with pytest.raises(FileNotFoundError, match="File not found"):
            create_zip_archive(['/path/to/nonexistent/file.txt'], temp_zip.name)
        
        # Clean up
        os.unlink(temp_zip.name)

def test_create_zip_archive_preserve_filenames(sample_files):
    """Test that original filenames are preserved in the zip archive."""
    with tempfile.NamedTemporaryFile(suffix='.zip', delete=False) as temp_zip:
        temp_zip.close()
        
        # Create zip archive
        create_zip_archive(sample_files, temp_zip.name)
        
        # Verify filenames in zip
        with zipfile.ZipFile(temp_zip.name, 'r') as zf:
            zip_contents = zf.namelist()
            for file in sample_files:
                assert os.path.basename(file) in zip_contents
        
        # Clean up
        os.unlink(temp_zip.name)