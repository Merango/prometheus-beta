import os
import pytest
from cryptography.fernet import Fernet
from src.file_decryption import decrypt_file, generate_key

@pytest.fixture
def sample_encrypted_file(tmpdir):
    """
    Create a sample encrypted file for testing
    """
    key = generate_key()
    fernet = Fernet(key)
    test_content = b"Hello, World! This is a test file."
    
    encrypted_file_path = os.path.join(tmpdir, "encrypted_test.bin")
    
    with open(encrypted_file_path, 'wb') as file:
        encrypted_data = fernet.encrypt(test_content)
        file.write(encrypted_data)
    
    return {
        'key': key,
        'file_path': encrypted_file_path,
        'content': test_content
    }

def test_successful_decryption(sample_encrypted_file):
    """
    Test successful file decryption
    """
    decrypted_data = decrypt_file(
        sample_encrypted_file['file_path'], 
        sample_encrypted_file['key']
    )
    assert decrypted_data == sample_encrypted_file['content']

def test_decrypt_with_string_key(sample_encrypted_file):
    """
    Test decryption with string key
    """
    key_str = sample_encrypted_file['key'].decode()
    decrypted_data = decrypt_file(
        sample_encrypted_file['file_path'], 
        key_str
    )
    assert decrypted_data == sample_encrypted_file['content']

def test_nonexistent_file():
    """
    Test decryption of non-existent file
    """
    with pytest.raises(FileNotFoundError):
        decrypt_file('/path/to/nonexistent/file.bin', generate_key())

def test_invalid_key(sample_encrypted_file):
    """
    Test decryption with invalid key
    """
    wrong_key = generate_key()  # Generate a different key
    with pytest.raises(ValueError):
        decrypt_file(sample_encrypted_file['file_path'], wrong_key)

def test_none_key():
    """
    Test decryption with None key
    """
    with pytest.raises(ValueError):
        decrypt_file('some_file.bin', None)

def test_invalid_key_type():
    """
    Test decryption with invalid key type
    """
    with pytest.raises(TypeError):
        decrypt_file('some_file.bin', 12345)

def test_generate_key():
    """
    Test key generation
    """
    key1 = generate_key()
    key2 = generate_key()
    
    assert isinstance(key1, bytes)
    assert len(key1) > 0
    assert key1 != key2  # Each generated key should be unique