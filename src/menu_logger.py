import logging
from typing import List, Any, Optional

class MenuLogger:
    """
    A class to handle logging of user menu selections.
    
    This class provides functionality to log user interactions with menus,
    supporting different logging levels and custom log file configuration.
    """
    
    def __init__(self, log_file: Optional[str] = None, log_level: int = logging.INFO):
        """
        Initialize the MenuLogger.
        
        Args:
            log_file (Optional[str]): Path to the log file. If None, logs to console.
            log_level (int): Logging level (default is logging.INFO).
        """
        # Configure logging
        self.logger = logging.getLogger('menu_logger')
        self.logger.setLevel(log_level)
        
        # Create formatter
        formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
        
        # Configure file handler if log_file is provided
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
        
        # Add console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
    
    def log_selection(self, menu_name: str, selection: Any) -> None:
        """
        Log a user's menu selection.
        
        Args:
            menu_name (str): Name or identifier of the menu.
            selection (Any): The selected item from the menu.
        
        Raises:
            ValueError: If menu_name is empty or selection is None.
        """
        # Validate inputs
        if not menu_name:
            raise ValueError("Menu name cannot be empty")
        
        if selection is None:
            raise ValueError("Selection cannot be None")
        
        # Log the selection
        log_message = f"Menu '{menu_name}' - Selected: {selection}"
        self.logger.info(log_message)
    
    def log_multiple_selections(self, menu_name: str, selections: List[Any]) -> None:
        """
        Log multiple selections from a menu.
        
        Args:
            menu_name (str): Name or identifier of the menu.
            selections (List[Any]): List of selected items.
        
        Raises:
            ValueError: If menu_name is empty or selections is empty.
        """
        # Validate inputs
        if not menu_name:
            raise ValueError("Menu name cannot be empty")
        
        if not selections:
            raise ValueError("Selections list cannot be empty")
        
        # Log multiple selections
        selections_str = ", ".join(str(sel) for sel in selections)
        log_message = f"Menu '{menu_name}' - Multiple Selections: {selections_str}"
        self.logger.info(log_message)