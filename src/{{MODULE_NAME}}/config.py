"""
Configuration module for {{PROJECT_NAME}}.
"""

from typing import Any

# Default configuration
DEFAULT_CONFIG: dict[str, Any] = {
    "setting1": "default_value1",
    "setting2": "default_value2",
    "debug": False,
    "log_level": "INFO",
}

# Global configuration instance
_config: dict[str, Any] = DEFAULT_CONFIG.copy()


def configure_settings(config: dict[str, Any]) -> None:
    """Configure global settings.

    Args:
        config: Configuration dictionary to merge with defaults
    """
    global _config
    _config.update(config)


def get_settings() -> dict[str, Any]:
    """Get current configuration settings.

    Returns:
        Current configuration dictionary
    """
    return _config.copy()


def get_setting(key: str, default: Any = None) -> Any:
    """Get a specific setting value.

    Args:
        key: Setting key to retrieve
        default: Default value if key not found

    Returns:
        Setting value or default
    """
    return _config.get(key, default)


def reset_settings() -> None:
    """Reset settings to defaults."""
    global _config
    _config = DEFAULT_CONFIG.copy()
