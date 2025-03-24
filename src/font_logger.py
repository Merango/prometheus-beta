"""
Module for logging output with different font sizes.

This module provides a function to log output with customizable font sizes,
supporting various size options and error handling.
"""
from enum import Enum, auto
from typing import Union, Optional


class FontSize(Enum):
    """Predefined font size options."""
    SMALL = auto()
    NORMAL = auto()
    LARGE = auto()
    EXTRA_LARGE = auto()


def log_output(
    message: str, 
    font_size: Union[FontSize, str] = FontSize.NORMAL, 
    prefix: Optional[str] = None
) -> str:
    """
    Log output with specified font size and optional prefix.

    Args:
        message (str): The message to be logged.
        font_size (FontSize, optional): The font size for the log message. 
            Defaults to FontSize.NORMAL.
        prefix (str, optional): An optional prefix to add to the message.

    Returns:
        str: The formatted log message.

    Raises:
        ValueError: If message is empty or font_size is invalid.
        TypeError: If message or prefix is not a string.
    """
    # Validate input
    if not isinstance(message, str):
        raise TypeError("Message must be a string")
    
    if message.strip() == "":
        raise ValueError("Message cannot be empty")
    
    # Normalize font_size if string is passed
    if isinstance(font_size, str):
        try:
            font_size = FontSize[font_size.upper()]
        except KeyError:
            raise ValueError(f"Invalid font size: {font_size}")
    
    # Optional prefix handling
    if prefix is not None:
        if not isinstance(prefix, str):
            raise TypeError("Prefix must be a string")
        message = f"{prefix} {message}"
    
    # Format message based on font size
    size_map = {
        FontSize.SMALL: f"🔹 {message}",
        FontSize.NORMAL: f"• {message}",
        FontSize.LARGE: f"🔸 {message}",
        FontSize.EXTRA_LARGE: f"🌟 {message}"
    }
    
    return size_map[font_size]