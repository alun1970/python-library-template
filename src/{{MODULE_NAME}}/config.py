"""
Configuration management for {{PROJECT_NAME}}.

This module handles configuration settings and validation.
"""

from typing import Any, Dict


# Default configuration
DEFAULT_CONFIG: Dict[str, Any] = {
    "setting1": "default_value1",
    "setting2": "default_value2",
    "debug": False,
}

# Global configuration instance
_config: Dict[str, Any] = DEFAULT_CONFIG.copy()


def configure_settings(config: Dict[str, Any]) -> None:
    """Configure global settings.
    
    Args:
        config: Configuration dictionary to merge with defaults
    """
    global _config
    _config.update(config)


def get_settings() -> Dict[str, Any]:
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
