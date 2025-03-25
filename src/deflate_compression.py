import zlib
from typing import Union

def deflate_compress(data: Union[str, bytes], compression_level: int = 6) -> bytes:
    """
    Compress data using the Deflate compression algorithm.

    Args:
        data (str or bytes): The input data to compress.
        compression_level (int, optional): Compression level from 0-9. 
            Defaults to 6 (default zlib compression level).
            0 = no compression, 9 = maximum compression.

    Returns:
        bytes: Compressed data using Deflate algorithm.

    Raises:
        TypeError: If input is not str or bytes.
        ValueError: If compression level is not between 0 and 9.
    """
    # Validate input type
    if not isinstance(data, (str, bytes)):
        raise TypeError("Input must be str or bytes")

    # Validate compression level
    if not 0 <= compression_level <= 9:
        raise ValueError("Compression level must be between 0 and 9")

    # Convert str to bytes if necessary
    if isinstance(data, str):
        data = data.encode('utf-8')

    # Use zlib to implement Deflate compression
    compressed_data = zlib.compress(data, compression_level)
    return compressed_data

def deflate_decompress(compressed_data: bytes) -> bytes:
    """
    Decompress data previously compressed with Deflate algorithm.

    Args:
        compressed_data (bytes): The compressed data to decompress.

    Returns:
        bytes: Decompressed original data.

    Raises:
        TypeError: If input is not bytes.
        zlib.error: If decompression fails due to corrupted data.
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")

    # Use zlib to decompress the data
    try:
        decompressed_data = zlib.decompress(compressed_data)
        return decompressed_data
    except zlib.error as e:
        raise zlib.error(f"Decompression failed: {str(e)}")