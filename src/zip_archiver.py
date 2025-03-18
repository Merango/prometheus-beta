import os
import zipfile
from typing import List, Union

def create_zip_archive(files: List[str], output_path: str) -> bool:
    """
    Create a zip archive containing multiple files.

    Args:
        files (List[str]): List of file paths to be added to the zip archive.
        output_path (str): Path where the zip archive will be created.

    Returns:
        bool: True if zip archive creation is successful, False otherwise.

    Raises:
        ValueError: If the input list is empty.
        FileNotFoundError: If any of the specified files do not exist.
    """
    # Validate input
    if not files:
        raise ValueError("File list cannot be empty")

    # Check if all files exist
    for file_path in files:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

    try:
        # Create the zip archive
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_path in files:
                # Add file to zip, preserving the file's base name
                zipf.write(file_path, os.path.basename(file_path))
        
        return True
    except Exception as e:
        # Log or handle any unexpected errors during zip creation
        print(f"Error creating zip archive: {e}")
        return False