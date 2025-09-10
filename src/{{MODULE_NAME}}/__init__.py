"""
{{PROJECT_NAME}} - {{PROJECT_DESCRIPTION}}

This package provides [brief description of functionality].

Key features:
- Feature 1
- Feature 2
- Feature 3
"""

from .config import configure_settings, get_settings
from .core import {{MAIN_CLASS}}, hello_world, main_function
from .utils import helper_function, utility_function

__version__ = "0.1.0"
__author__ = "{{AUTHOR_NAME}}"
__email__ = "{{AUTHOR_EMAIL}}"

__all__ = [
    # Core functionality
    "{{MAIN_CLASS}}",
    "main_function",
    "hello_world",
    # Configuration
    "configure_settings",
    "get_settings",
    # Utilities
    "utility_function",
    "helper_function",
]
