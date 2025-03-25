"""
Module for merging multiple files into a single file.

This module provides functionality to combine the contents of multiple files
into a single output file, with optional configuration for handling different 
scenarios.
"""

import os
from typing import List, Union


def merge_files(input_files: List[str], output_file: str, separator: str = '\n\n') -> None:
    """
    Merge the contents of multiple input files into a single output file.

    Args:
        input_files (List[str]): List of paths to input files to be merged.
        output_file (str): Path to the output file where merged contents will be written.
        separator (str, optional): String to insert between file contents. 
                                   Defaults to two newline characters.

    Raises:
        ValueError: If input_files is empty or contains non-existent files.
        IOError: If there are issues reading input files or writing output file.
    """
    # Validate input files
    if not input_files:
        raise ValueError("No input files provided")

    # Check that all input files exist
    non_existent_files = [f for f in input_files if not os.path.exists(f)]
    if non_existent_files:
        raise ValueError(f"The following files do not exist: {non_existent_files}")

    try:
        # Open output file in write mode
        with open(output_file, 'w', encoding='utf-8') as outfile:
            # Iterate through input files
            for i, input_file in enumerate(input_files):
                # Read contents of each input file
                with open(input_file, 'r', encoding='utf-8') as infile:
                    file_contents = infile.read()
                
                # Write file contents to output file
                outfile.write(file_contents)
                
                # Add separator between files, but not after the last file
                if i < len(input_files) - 1:
                    outfile.write(separator)

    except IOError as e:
        # Catch and re-raise any IO-related errors with more context
        raise IOError(f"Error merging files: {e}") from e