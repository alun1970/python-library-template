"""
Core functionality for {{PROJECT_NAME}}.

This module contains the main classes and functions for the package.
"""

from typing import Any


class {{MAIN_CLASS}}:
    """Main class for {{PROJECT_NAME}}."""

    def __init__(self, config: dict[str, Any] | None = None) -> None:
        """Initialize {{MAIN_CLASS}}.

        Args:
            config: Optional configuration dictionary
        """
        self.config = config or {}

    def hello_world(self, name: str | None = None) -> str:
        """Return a Hello World greeting.

        Args:
            name: Optional name to include in greeting

        Returns:
            Hello World greeting string
        """
        if name:
            return f"Hello, {name}! Welcome to {{PROJECT_NAME}}!"
        return "Hello, World! Welcome to {{PROJECT_NAME}}!"

    def process(self, data: Any) -> Any:
        """Process data using the configured settings.

        Args:
            data: Input data to process

        Returns:
            Processed data
        """
        # Implementation here
        return f"Processed: {data}"

    def advanced_process(self, data: Any, options: dict[str, Any] | None = None) -> Any:
        """Advanced processing with additional options.

        Args:
            data: Input data to process
            options: Additional processing options

        Returns:
            Processed data with advanced features
        """
        options = options or {}
        # Implementation here
        return f"Advanced processed: {data} with options {options}"


def hello_world(name: str | None = None) -> str:
    """Return a Hello World greeting.

    Args:
        name: Optional name to include in greeting

    Returns:
        Hello World greeting string
    """
    if name:
        return f"Hello, {name}! Welcome to {{PROJECT_NAME}}!"
    return "Hello, World! Welcome to {{PROJECT_NAME}}!"


def main_function(data: Any) -> Any:
    """Main function for simple operations.

    Args:
        data: Input data

    Returns:
        Processed result
    """
    instance = {{MAIN_CLASS}}()
    return instance.process(data)


class {{MODULE_NAME}}Error(Exception):
    """Base exception for {{PROJECT_NAME}}."""

    pass


class ConfigurationError({{MODULE_NAME}}Error):
    """Raised when there's a configuration error."""

    pass


class ProcessingError({{MODULE_NAME}}Error):
    """Raised when processing fails."""

    pass
