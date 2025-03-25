import pytest
import zlib
from src.zlib_compression import compress_data, decompress_data

def test_compress_string():
    """Test compressing a string"""
    original = "Hello, world! This is a test of Zlib compression."
    compressed = compress_data(original)
    assert isinstance(compressed, bytes)
    assert len(compressed) < len(original.encode('utf-8'))

def test_compress_bytes():
    """Test compressing bytes"""
    original = b"Binary data compression test"
    compressed = compress_data(original)
    assert isinstance(compressed, bytes)
    assert len(compressed) < len(original)

def test_decompress_data():
    """Test decompressing data"""
    original = "Hello, world! This is a test of Zlib compression."
    compressed = compress_data(original)
    decompressed = decompress_data(compressed)
    assert decompressed.decode('utf-8') == original

def test_compression_levels():
    """Test different compression levels"""
    data = "Test compression levels" * 100
    compressed_low = compress_data(data, compression_level=1)
    compressed_mid = compress_data(data, compression_level=6)
    compressed_high = compress_data(data, compression_level=9)
    
    assert len(compressed_low) > 0
    assert len(compressed_mid) > 0
    assert len(compressed_high) > 0
    assert len(compressed_low) >= len(compressed_high)

def test_invalid_input_type():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        compress_data(123)
    
    with pytest.raises(TypeError):
        decompress_data("not bytes")

def test_invalid_compression_level():
    """Test handling of invalid compression levels"""
    with pytest.raises(ValueError):
        compress_data("data", compression_level=-1)
    
    with pytest.raises(ValueError):
        compress_data("data", compression_level=10)

def test_decompress_invalid_data():
    """Test decompression of invalid compressed data"""
    with pytest.raises(zlib.error):
        decompress_data(b"invalid compressed data")

def test_round_trip_compression():
    """Test full compression and decompression cycle"""
    test_cases = [
        "Hello, world!",
        "Test with some longer text to ensure proper compression",
        b"Binary data test",
        "🌍 Unicode test"  # Test with unicode characters
    ]
    
    for original in test_cases:
        if isinstance(original, str):
            original_bytes = original.encode('utf-8')
        else:
            original_bytes = original
        
        compressed = compress_data(original)
        decompressed = decompress_data(compressed)
        
        assert decompressed == original_bytes