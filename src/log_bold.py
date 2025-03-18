def log_bold(message):
    """
    Log a message in bold text to the console.

    Args:
        message (str): The message to be logged in bold.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input is an empty string.

    Returns:
        str: The bold-formatted message.
    """
    # Validate input
    if not isinstance(message, str):
        raise TypeError("Input must be a string")
    
    if not message:
        raise ValueError("Message cannot be empty")
    
    # ANSI escape codes for bold text
    BOLD_START = "\033[1m"
    BOLD_END = "\033[0m"
    
    # Format and print the message
    bold_message = f"{BOLD_START}{message}{BOLD_END}"
    print(bold_message)
    
    return bold_message