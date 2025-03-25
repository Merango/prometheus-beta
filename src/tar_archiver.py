import os
import tarfile
from typing import Union, Optional


def create_tar_archive(source_dir: str, 
                       archive_path: Optional[str] = None, 
                       compression: str = 'gz') -> str:
    """
    Create a tar archive of a given directory.

    Args:
        source_dir (str): Path to the directory to be archived
        archive_path (Optional[str], optional): Path for the output archive. 
            If None, creates archive in the same directory as source.
        compression (str, optional): Compression type. 
            Supports 'gz' (default), 'bz2', or 'xz'.

    Returns:
        str: Path to the created archive

    Raises:
        ValueError: If source directory does not exist or is not a directory
        ValueError: If invalid compression type is specified
    """
    # Validate source directory
    source_dir = os.path.abspath(source_dir)
    if not os.path.exists(source_dir):
        raise ValueError(f"Source directory does not exist: {source_dir}")
    
    if not os.path.isdir(source_dir):
        raise ValueError(f"Source path is not a directory: {source_dir}")

    # Validate compression type
    valid_compressions = {'gz', 'bz2', 'xz'}
    if compression not in valid_compressions:
        raise ValueError(f"Invalid compression type. Must be one of {valid_compressions}")

    # Determine archive path
    if archive_path is None:
        # Use source directory name as base for archive name
        dir_name = os.path.basename(source_dir.rstrip('/'))
        archive_path = os.path.join(
            os.path.dirname(source_dir), 
            f"{dir_name}.tar.{compression}"
        )

    # Ensure archive path has correct extension
    if not archive_path.endswith(f'.tar.{compression}'):
        archive_path = f"{archive_path}.tar.{compression}"

    # Create tar archive
    try:
        with tarfile.open(archive_path, f'w:{compression}') as tar:
            tar.add(source_dir, arcname=os.path.basename(source_dir))
    except PermissionError:
        raise PermissionError(f"Permission denied when creating archive: {archive_path}")
    except Exception as e:
        raise RuntimeError(f"Error creating tar archive: {str(e)}")

    return archive_path