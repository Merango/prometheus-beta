import os
import bz2
import pytest
from src.bzip2_decompressor import decompress_bzip2_file

@pytest.fixture
def sample_bzip2_file(tmp_path):
    """Create a sample bzip2 compressed file for testing."""
    input_text = "This is a test file for bzip2 decompression."
    compressed_file = tmp_path / "sample.txt.bz2"
    
    with bz2.open(compressed_file, 'wb') as f:
        f.write(input_text.encode('utf-8'))
    
    return compressed_file

def test_successful_decompression(sample_bzip2_file, tmp_path):
    """Test successful file decompression."""
    output_path = tmp_path / "decompressed.txt"
    result = decompress_bzip2_file(str(sample_bzip2_file), str(output_path))
    
    assert os.path.exists(result)
    with open(result, 'r') as f:
        content = f.read()
    assert content == "This is a test file for bzip2 decompression."

def test_default_output_path(sample_bzip2_file):
    """Test decompression with default output path."""
    result = decompress_bzip2_file(str(sample_bzip2_file))
    
    assert os.path.exists(result)
    assert result == str(sample_bzip2_file).removesuffix('.bz2')

def test_nonexistent_file():
    """Test handling of nonexistent input file."""
    with pytest.raises(FileNotFoundError):
        decompress_bzip2_file("nonexistent_file.bz2")

def test_directory_input(tmp_path):
    """Test handling of directory input."""
    with pytest.raises(IsADirectoryError):
        decompress_bzip2_file(str(tmp_path))

def test_permission_error(sample_bzip2_file, mocker):
    """Test handling of permission errors."""
    # Mock open to raise PermissionError
    mocker.patch('builtins.open', side_effect=PermissionError)
    
    with pytest.raises(PermissionError):
        decompress_bzip2_file(str(sample_bzip2_file), "/path/with/no/permission/output.txt")

def test_corrupted_bzip2_file(tmp_path):
    """Test handling of corrupted bzip2 file."""
    corrupted_file = tmp_path / "corrupted.bz2"
    
    # Create a file that looks like a bzip2 file but is corrupted
    with open(corrupted_file, 'wb') as f:
        f.write(b'This is not a valid bzip2 file')
    
    with pytest.raises(bz2.BZ2Error):
        decompress_bzip2_file(str(corrupted_file))