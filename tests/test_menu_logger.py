import os
import logging
import pytest
import tempfile
from src.menu_logger import MenuLogger

class TestMenuLogger:
    @pytest.fixture
    def temp_log_file(self):
        """Create a temporary log file for testing."""
        with tempfile.NamedTemporaryFile(delete=False, mode='w+', suffix='.log') as temp_file:
            temp_file_path = temp_file.name
        yield temp_file_path
        # Clean up the temporary file
        os.unlink(temp_file_path)
    
    def test_single_selection_logging(self, temp_log_file, caplog):
        """Test logging a single menu selection."""
        caplog.set_level(logging.INFO)
        logger = MenuLogger(log_file=temp_log_file)
        
        # Log a selection
        logger.log_selection("Main Menu", "Option 1")
        
        # Check console log
        assert "Menu 'Main Menu' - Selected: Option 1" in caplog.text
        
        # Check file log
        with open(temp_log_file, 'r') as f:
            log_contents = f.read()
            assert "Menu 'Main Menu' - Selected: Option 1" in log_contents
    
    def test_multiple_selections_logging(self, temp_log_file, caplog):
        """Test logging multiple menu selections."""
        caplog.set_level(logging.INFO)
        logger = MenuLogger(log_file=temp_log_file)
        
        # Log multiple selections
        logger.log_multiple_selections("Settings Menu", ["Dark Mode", "Notifications"])
        
        # Check console log
        assert "Menu 'Settings Menu' - Multiple Selections: Dark Mode, Notifications" in caplog.text
        
        # Check file log
        with open(temp_log_file, 'r') as f:
            log_contents = f.read()
            assert "Menu 'Settings Menu' - Multiple Selections: Dark Mode, Notifications" in log_contents
    
    def test_invalid_single_selection_inputs(self):
        """Test error handling for invalid single selection inputs."""
        logger = MenuLogger()
        
        # Test empty menu name
        with pytest.raises(ValueError, match="Menu name cannot be empty"):
            logger.log_selection("", "Option 1")
        
        # Test None selection
        with pytest.raises(ValueError, match="Selection cannot be None"):
            logger.log_selection("Main Menu", None)
    
    def test_invalid_multiple_selections_inputs(self):
        """Test error handling for invalid multiple selections inputs."""
        logger = MenuLogger()
        
        # Test empty menu name
        with pytest.raises(ValueError, match="Menu name cannot be empty"):
            logger.log_multiple_selections("", ["Option 1"])
        
        # Test empty selections list
        with pytest.raises(ValueError, match="Selections list cannot be empty"):
            logger.log_multiple_selections("Main Menu", [])