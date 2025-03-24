"""
Tests for the font_logger module.

This module contains comprehensive tests for the log_output function,
covering various scenarios and edge cases.
"""
import pytest
from src.font_logger import log_output, FontSize


def test_normal_log():
    """Test default (normal) log output."""
    result = log_output("Test message")
    assert result == "• Test message"


def test_different_font_sizes():
    """Test all predefined font sizes."""
    assert log_output("Small", FontSize.SMALL).startswith("🔹")
    assert log_output("Normal", FontSize.NORMAL).startswith("•")
    assert log_output("Large", FontSize.LARGE).startswith("🔸")
    assert log_output("Extra Large", FontSize.EXTRA_LARGE).startswith("🌟")


def test_font_size_string_input():
    """Test font size input as string."""
    assert log_output("Small", "SMALL").startswith("🔹")
    assert log_output("Large", "LARGE").startswith("🔸")


def test_log_with_prefix():
    """Test log output with a prefix."""
    result = log_output("Message", prefix="PREFIX:")
    assert result == "• PREFIX: Message"
    
    result_large = log_output("Message", FontSize.LARGE, prefix="PREFIX:")
    assert result_large.startswith("🔸") and "PREFIX: Message" in result_large


def test_invalid_font_size():
    """Test handling of invalid font size."""
    with pytest.raises(ValueError, match="Invalid font size"):
        log_output("Test", "INVALID_SIZE")


def test_empty_message():
    """Test handling of empty message."""
    with pytest.raises(ValueError, match="Message cannot be empty"):
        log_output("")
    with pytest.raises(ValueError, match="Message cannot be empty"):
        log_output("   ")


def test_invalid_message_type():
    """Test handling of non-string message."""
    with pytest.raises(TypeError, match="Message must be a string"):
        log_output(123)


def test_invalid_prefix_type():
    """Test handling of non-string prefix."""
    with pytest.raises(TypeError, match="Prefix must be a string"):
        log_output("Message", prefix=123)