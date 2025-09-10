"""Test configuration and fixtures."""

import pytest


@pytest.fixture
def sample_data():
    """Provide sample data for tests."""
    return {
        "text": "Hello, World!",
        "number": 42,
        "list": [1, 2, 3, 4, 5],
        "dict": {"key": "value"}
    }


@pytest.fixture
def sample_config():
    """Provide sample configuration for tests."""
    return {
        "setting1": "test_value1",
        "setting2": "test_value2",
        "debug": True
    }
