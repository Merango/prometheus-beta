"""
Unit tests for LZVN compression algorithm implementation
"""

import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzvn_compression import compress, decompress

def test_compress_decompress_basic():
    """Test basic compression and decompression"""
    original_data = b"hello world" * 10
    compressed = compress(original_data)
    assert compressed is not None
    assert len(compressed) < len(original_data)
    
    decompressed = decompress(compressed)
    assert decompressed == original_data

def test_compress_decompress_repeated_pattern():
    """Test compression of repeated patterns"""
    original_data = b"\x00" * 100 + b"\xFF" * 50
    compressed = compress(original_data)
    assert compressed is not None
    
    decompressed = decompress(compressed)
    assert decompressed == original_data

def test_input_type_validation():
    """Test input type validation for both compress and decompress"""
    with pytest.raises(TypeError):
        compress("not bytes")
    
    with pytest.raises(TypeError):
        decompress("not bytes")

def test_empty_input():
    """Test handling of empty input"""
    with pytest.raises(ValueError):
        compress(b"")
    
    with pytest.raises(ValueError):
        decompress(b"")

def test_complex_data():
    """Test compression of more complex data"""
    original_data = b"This is a test of the LZVN compression algorithm " * 20
    compressed = compress(original_data)
    assert compressed is not None
    assert len(compressed) < len(original_data)
    
    decompressed = decompress(compressed)
    assert decompressed == original_data

def test_binary_data():
    """Test compression of binary data"""
    original_data = bytes([i % 256 for i in range(1000)])
    compressed = compress(original_data)
    assert compressed is not None
    
    decompressed = decompress(compressed)
    assert decompressed == original_data

def test_random_data():
    """Test compression of pseudo-random data"""
    import random
    random.seed(42)  # Consistent seed for reproducibility
    original_data = bytes(random.getrandbits(8) for _ in range(1000))
    compressed = compress(original_data)
    
    decompressed = decompress(compressed)
    assert decompressed == original_data