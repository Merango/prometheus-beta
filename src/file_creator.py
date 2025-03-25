import os

def create_text_file(file_path, content=''):
    """
    Create a new text file with optional content.

    Args:
        file_path (str): The path where the file should be created.
        content (str, optional): The content to write to the file. Defaults to empty string.

    Raises:
        ValueError: If file_path is empty or None.
        OSError: If the file cannot be created due to permission or path issues.
    """
    # Validate input
    if not file_path:
        raise ValueError("File path cannot be empty")

    # Ensure directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True) if os.path.dirname(file_path) else None

    # Create and write to file
    try:
        with open(file_path, 'w') as f:
            f.write(content)
        return True
    except Exception as e:
        raise OSError(f"Could not create file at {file_path}: {str(e)}")