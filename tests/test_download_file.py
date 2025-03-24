import os
import pytest
import requests
import tempfile
from unittest.mock import patch

from src.download_file import download_file

class MockResponse:
    def __init__(self, content=b'test content', status_code=200, headers=None):
        self.content = content
        self.status_code = status_code
        self.headers = headers or {}
        self.iter_content_counter = 0

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"HTTP Error {self.status_code}")

    def iter_content(self, chunk_size=1):
        yield self.content

def test_download_file_default_filename(tmp_path):
    """Test downloading a file with default filename."""
    test_url = 'http://example.com/testfile.txt'
    mock_response = MockResponse(content=b'test download content')

    with patch('requests.get', return_value=mock_response):
        os.chdir(tmp_path)
        result_path = download_file(test_url)
        
        assert os.path.exists(result_path)
        assert os.path.basename(result_path) == 'testfile.txt'
        
        with open(result_path, 'rb') as f:
            assert f.read() == b'test download content'

def test_download_file_with_custom_path(tmp_path):
    """Test downloading a file with a custom destination path."""
    test_url = 'http://example.com/testfile.txt'
    custom_path = os.path.join(tmp_path, 'custom_download.txt')
    mock_response = MockResponse(content=b'test custom content')

    with patch('requests.get', return_value=mock_response):
        os.chdir(tmp_path)
        result_path = download_file(test_url, custom_path)
        
        assert result_path == os.path.abspath(custom_path)
        assert os.path.exists(result_path)
        
        with open(result_path, 'rb') as f:
            assert f.read() == b'test custom content'

def test_download_file_invalid_url():
    """Test handling of invalid URL."""
    with pytest.raises(ValueError):
        download_file('')
    
    with pytest.raises(ValueError):
        download_file(None)

def test_download_file_network_error():
    """Test handling of network errors."""
    with patch('requests.get', side_effect=requests.RequestException("Network error")):
        with pytest.raises(RuntimeError, match="Error downloading file"):
            download_file('http://example.com/nonexistent')

def test_download_file_http_error():
    """Test handling of HTTP errors."""
    mock_response = MockResponse(status_code=404)
    with patch('requests.get', return_value=mock_response):
        with pytest.raises(RuntimeError):
            download_file('http://example.com/404')

def test_download_file_ensures_download_directory(tmp_path):
    """Test that download directory is created if it doesn't exist."""
    test_url = 'http://example.com/testfile.txt'
    download_path = os.path.join(tmp_path, 'new_dir', 'testfile.txt')
    mock_response = MockResponse(content=b'test directory creation')

    with patch('requests.get', return_value=mock_response):
        os.chdir(tmp_path)
        result_path = download_file(test_url, download_path)
        
        assert os.path.exists(result_path)
        assert os.path.exists(os.path.dirname(result_path))