import pytest
import zlib
from src.deflate_compression import deflate_compress, deflate_decompress

def test_compress_decompress_text():
    """Test compression and decompression of text data."""
    original_text = "Hello, Deflate compression algorithm!"
    compressed = deflate_compress(original_text)
    decompressed = deflate_decompress(compressed)
    assert decompressed.decode('utf-8') == original_text

def test_compress_decompress_bytes():
    """Test compression and decompression of byte data."""
    original_bytes = b'\x00\x01\x02\x03\x04'
    compressed = deflate_compress(original_bytes)
    decompressed = deflate_decompress(compressed)
    assert decompressed == original_bytes

def test_different_compression_levels():
    """Test compression with different compression levels."""
    text = "Test compression levels" * 100
    for level in range(10):
        compressed = deflate_compress(text, level)
        decompressed = deflate_decompress(compressed)
        assert decompressed.decode('utf-8') == text

def test_invalid_input_type():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        deflate_compress(123)
    with pytest.raises(TypeError):
        deflate_decompress("not bytes")

def test_invalid_compression_level():
    """Test error handling for invalid compression levels."""
    with pytest.raises(ValueError):
        deflate_compress("test", -1)
    with pytest.raises(ValueError):
        deflate_compress("test", 10)

def test_empty_input():
    """Test compression and decompression of empty data."""
    empty_text = ""
    empty_bytes = b''
    
    compressed_text = deflate_compress(empty_text)
    compressed_bytes = deflate_compress(empty_bytes)
    
    assert deflate_decompress(compressed_text) == b''
    assert deflate_decompress(compressed_bytes) == b''

def test_large_input():
    """Test compression and decompression of large data."""
    large_text = "Large data test " * 10000
    compressed = deflate_compress(large_text)
    decompressed = deflate_decompress(compressed)
    assert decompressed.decode('utf-8') == large_text

def test_corrupted_data():
    """Test error handling for corrupted compressed data."""
    with pytest.raises(zlib.error):
        deflate_decompress(b'corrupted data')