"""
Utility functions for {{PROJECT_NAME}}.

This module contains helper functions and utilities.
"""

from typing import Any, List, Optional


def utility_function(data: Any) -> str:
    """A utility function that processes data.
    
    Args:
        data: Input data to process
        
    Returns:
        Processed string representation
    """
    return f"Utility processed: {data}"


def helper_function(items: List[Any], transform: bool = False) -> List[Any]:
    """Helper function to process a list of items.
    
    Args:
        items: List of items to process
        transform: Whether to apply transformation
        
    Returns:
        Processed list of items
    """
    if transform:
        return [f"Transformed: {item}" for item in items]
    return items.copy()


def validate_input(data: Any, required_type: type) -> bool:
    """Validate input data type.
    
    Args:
        data: Data to validate
        required_type: Expected type
        
    Returns:
        True if data is of required type
    """
    return isinstance(data, required_type)


def format_output(data: Any, format_type: str = "string") -> str:
    """Format output data.
    
    Args:
        data: Data to format
        format_type: Format type (string, json, etc.)
        
    Returns:
        Formatted string
    """
    if format_type == "json":
        import json
        return json.dumps(data, indent=2)
    return str(data)


def safe_divide(a: float, b: float, default: Optional[float] = None) -> Optional[float]:
    """Safely divide two numbers.
    
    Args:
        a: Numerator
        b: Denominator  
        default: Default value if division by zero
        
    Returns:
        Result of division or default value
    """
    if b == 0:
        return default
    return a / b
