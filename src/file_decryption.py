from cryptography.fernet import Fernet
import os

def decrypt_file(encrypted_file_path, key):
    """
    Decrypt an encrypted file using Fernet symmetric encryption.
    
    Args:
        encrypted_file_path (str): Path to the encrypted file
        key (bytes or str): Encryption key used for decryption
    
    Returns:
        bytes: Decrypted file contents
    
    Raises:
        FileNotFoundError: If the encrypted file does not exist
        ValueError: If the key is invalid or None
        TypeError: If key is not bytes or str
    """
    # Validate input first
    if key is None:
        raise ValueError("Encryption key cannot be None")
    
    if not encrypted_file_path:
        raise ValueError("Encrypted file path cannot be empty")
    
    if not os.path.exists(encrypted_file_path):
        raise FileNotFoundError(f"File not found: {encrypted_file_path}")
    
    # Convert key to bytes if it's a string
    if isinstance(key, str):
        key = key.encode()
    
    if not isinstance(key, bytes):
        raise TypeError("Key must be bytes or str")
    
    try:
        # Create a Fernet instance with the key
        fernet = Fernet(key)
        
        # Read the encrypted file
        with open(encrypted_file_path, 'rb') as file:
            encrypted_data = file.read()
        
        # Decrypt the data
        decrypted_data = fernet.decrypt(encrypted_data)
        
        return decrypted_data
    
    except Exception as e:
        # Generic error handling for decryption failures
        raise ValueError(f"Decryption failed: {str(e)}")

def generate_key():
    """
    Generate a new Fernet encryption key.
    
    Returns:
        bytes: A new encryption key
    """
    return Fernet.generate_key()