import os
import shutil

def delete_empty_directory(path):
    """
    Delete an empty directory.

    Args:
        path (str): Path to the directory to be deleted.

    Raises:
        FileNotFoundError: If the directory does not exist.
        OSError: If the directory is not empty or cannot be deleted.
        ValueError: If the path is not a directory.

    Returns:
        bool: True if the directory was successfully deleted.
    """
    # Validate input path
    if not os.path.exists(path):
        raise FileNotFoundError(f"Directory not found: {path}")
    
    # Check if path is a directory
    if not os.path.isdir(path):
        raise ValueError(f"Path is not a directory: {path}")
    
    # Check if directory is empty
    if os.listdir(path):
        raise OSError(f"Directory is not empty: {path}")
    
    try:
        os.rmdir(path)
        return True
    except PermissionError:
        raise OSError(f"Permission denied to delete directory: {path}")