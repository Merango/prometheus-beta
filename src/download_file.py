import os
import requests

def download_file(url, destination_path=None):
    """
    Download a file from a given URL.

    Args:
        url (str): The URL of the file to download.
        destination_path (str, optional): Path to save the downloaded file. 
                                          If not provided, uses the filename from the URL.

    Returns:
        str: The full path where the file was saved.

    Raises:
        ValueError: If the URL is invalid or empty.
        RequestException: If there's an error downloading the file.
        IOError: If there's an issue saving the file.
    """
    # Validate URL
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL provided")

    try:
        # Send a GET request to download the file
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Determine destination path
        if destination_path is None:
            # Extract filename from URL or Content-Disposition header
            filename = response.headers.get('Content-Disposition')
            if filename:
                filename = filename.split('filename=')[-1].strip('"')
            else:
                filename = url.split('/')[-1]
            
            # Use current directory if no path specified
            destination_path = os.path.join('downloads', filename)

        # Ensure the download directory exists
        os.makedirs(os.path.dirname(destination_path), exist_ok=True)

        # Write the file
        with open(destination_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        return os.path.abspath(destination_path)

    except requests.RequestException as e:
        raise RuntimeError(f"Error downloading file: {str(e)}")
    except IOError as e:
        raise IOError(f"Error saving file: {str(e)}")