def log_array_as_table(arr, headers=None, column_width=20):
    """
    Log an array in a formatted table.

    Args:
        arr (list): The array to be logged.
        headers (list, optional): Column headers for the table. 
                                  Defaults to None.
        column_width (int, optional): Width of each column. 
                                      Defaults to 20.

    Returns:
        str: Formatted table as a string.

    Raises:
        TypeError: If input is not a list.
        ValueError: If headers length doesn't match array element length.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty array
    if not arr:
        return "Empty array"
    
    # Determine if we're dealing with nested data
    is_nested = any(isinstance(item, (list, tuple, dict)) for item in arr)
    
    # Prepare headers
    if headers is None:
        if is_nested:
            # Generate generic headers if not provided
            headers = [f'Column {i+1}' for i in range(len(max(arr, key=len) if arr else 0))]
        else:
            headers = ['Value']
    
    # Validate headers
    if is_nested and len(headers) != len(max(arr, key=len)):
        raise ValueError("Headers must match the number of columns in the array")
    
    # Convert all items to strings for consistent formatting
    def format_item(item):
        if item is None:
            return 'None'
        return str(item)
    
    # Prepare table
    table_lines = []
    
    # Add header
    header_line = ''.join(h.ljust(column_width) for h in headers)
    table_lines.append(header_line)
    table_lines.append('-' * len(header_line))
    
    # Add rows
    for row in arr:
        # Handle different types of rows
        if not isinstance(row, (list, tuple, dict)):
            row = [row]
        
        # Convert row to list if it's a dict
        if isinstance(row, dict):
            row = [row.get(h, 'N/A') for h in headers]
        
        # Format and pad row
        formatted_row = ''.join(format_item(item).ljust(column_width) for item in row)
        table_lines.append(formatted_row)
    
    return '\n'.join(table_lines)