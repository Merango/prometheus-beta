import os
import typing

def create_directory(path: str, mode: int = 0o755, parents: bool = False) -> typing.Dict[str, typing.Any]:
    """
    Create a new directory with optional parent directory creation.

    Args:
        path (str): The path of the directory to create
        mode (int, optional): The file mode (permissions) for the new directory. Defaults to 0o755.
        parents (bool, optional): If True, create parent directories if they don't exist. Defaults to False.

    Returns:
        dict: A dictionary with creation status and details

    Raises:
        ValueError: If path is None or empty
        PermissionError: If insufficient permissions to create directory
        FileExistsError: If directory already exists and parents is False
    """
    # Validate input
    if not path:
        raise ValueError("Directory path cannot be None or empty")

    # Normalize path to remove any trailing separators
    path = os.path.normpath(path)

    try:
        # Determine directory creation method based on parents flag
        if parents:
            os.makedirs(path, mode=mode, exist_ok=True)
        else:
            os.mkdir(path, mode=mode)

        return {
            "success": True,
            "path": path,
            "created": True,
            "mode": mode
        }
    except PermissionError:
        return {
            "success": False,
            "path": path,
            "created": False,
            "error": "Permission denied"
        }
    except FileExistsError:
        return {
            "success": False,
            "path": path,
            "created": False,
            "error": "Directory already exists"
        }
    except Exception as e:
        return {
            "success": False,
            "path": path,
            "created": False,
            "error": str(e)
        }