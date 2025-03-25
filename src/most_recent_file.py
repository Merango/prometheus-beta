import os
from typing import Optional, Union

def find_most_recent_file(directory: Union[str, os.PathLike]) -> Optional[str]:
    """
    Find the most recently modified file in a given directory.

    Args:
        directory (str or os.PathLike): Path to the directory to search.

    Returns:
        Optional[str]: Path to the most recently modified file, or None if 
                       the directory is empty or cannot be accessed.

    Raises:
        NotADirectoryError: If the provided path is not a directory.
        PermissionError: If there are insufficient permissions to access the directory.
    """
    # Validate input
    if not os.path.exists(directory):
        return None
    
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"{directory} is not a directory")
    
    try:
        # Check if directory is readable
        os.listdir(directory)
    except PermissionError:
        raise PermissionError(f"Cannot access directory {directory}: Permission denied")
    
    try:
        # Get all files in the directory
        files = [
            os.path.join(directory, f) for f in os.listdir(directory) 
            if os.path.isfile(os.path.join(directory, f))
        ]
        
        # If no files, return None
        if not files:
            return None
        
        # Find the most recently modified file
        return max(files, key=os.path.getmtime)
    
    except (OSError) as e:
        # Handle other OS-related errors
        raise PermissionError(f"Cannot access directory {directory}: {str(e)}")