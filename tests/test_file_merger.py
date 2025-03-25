"""
Tests for the file merger functionality.
"""

import os
import pytest
import tempfile
from src.file_merger import merge_files


def test_merge_files_basic():
    """Test basic file merging functionality."""
    # Create temporary files
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create input files
        input1 = os.path.join(tmpdir, 'file1.txt')
        input2 = os.path.join(tmpdir, 'file2.txt')
        output = os.path.join(tmpdir, 'merged.txt')
        
        with open(input1, 'w') as f1:
            f1.write("Hello")
        
        with open(input2, 'w') as f2:
            f2.write("World")
        
        # Merge files
        merge_files([input1, input2], output)
        
        # Verify merged content
        with open(output, 'r') as merged:
            content = merged.read()
            assert content == "Hello\n\nWorld"


def test_merge_files_custom_separator():
    """Test merging files with a custom separator."""
    with tempfile.TemporaryDirectory() as tmpdir:
        input1 = os.path.join(tmpdir, 'file1.txt')
        input2 = os.path.join(tmpdir, 'file2.txt')
        output = os.path.join(tmpdir, 'merged.txt')
        
        with open(input1, 'w') as f1:
            f1.write("Hello")
        
        with open(input2, 'w') as f2:
            f2.write("World")
        
        # Merge files with custom separator
        merge_files([input1, input2], output, separator=' --- ')
        
        # Verify merged content
        with open(output, 'r') as merged:
            content = merged.read()
            assert content == "Hello --- World"


def test_merge_files_empty_input():
    """Test that an empty input list raises a ValueError."""
    with tempfile.TemporaryDirectory() as tmpdir:
        output = os.path.join(tmpdir, 'merged.txt')
        
        with pytest.raises(ValueError, match="No input files provided"):
            merge_files([], output)


def test_merge_files_non_existent():
    """Test that non-existent files raise a ValueError."""
    with tempfile.TemporaryDirectory() as tmpdir:
        output = os.path.join(tmpdir, 'merged.txt')
        non_existent_file = os.path.join(tmpdir, 'non_existent.txt')
        
        with pytest.raises(ValueError, match="do not exist"):
            merge_files([non_existent_file], output)


def test_merge_files_multiple_inputs():
    """Test merging multiple input files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        input1 = os.path.join(tmpdir, 'file1.txt')
        input2 = os.path.join(tmpdir, 'file2.txt')
        input3 = os.path.join(tmpdir, 'file3.txt')
        output = os.path.join(tmpdir, 'merged.txt')
        
        with open(input1, 'w') as f1:
            f1.write("First")
        
        with open(input2, 'w') as f2:
            f2.write("Second")
        
        with open(input3, 'w') as f3:
            f3.write("Third")
        
        # Merge files
        merge_files([input1, input2, input3], output)
        
        # Verify merged content
        with open(output, 'r') as merged:
            content = merged.read()
            assert content == "First\n\nSecond\n\nThird"