# API Reference

## Core Classes

### {{MAIN_CLASS}}

The main class for {{PROJECT_NAME}}.

```python
from {{MODULE_NAME}} import {{MAIN_CLASS}}

instance = {{MAIN_CLASS}}(config=None)
```

#### Parameters

- `config` (dict, optional): Configuration dictionary

#### Methods

##### `process(data)`

Process data using the configured settings.

**Parameters:**
- `data`: Input data to process

**Returns:**
- Processed data

**Example:**
```python
instance = {{MAIN_CLASS}}()
result = instance.process("Hello, World!")
```

##### `advanced_process(data, options=None)`

Advanced processing with additional options.

**Parameters:**
- `data`: Input data to process
- `options` (dict, optional): Additional processing options

**Returns:**
- Processed data with advanced features

**Example:**
```python
instance = {{MAIN_CLASS}}()
options = {"mode": "advanced"}
result = instance.advanced_process("data", options)
```

## Functions

### `main_function(data)`

Main function for simple operations.

**Parameters:**
- `data`: Input data

**Returns:**
- Processed result

**Example:**
```python
from {{MODULE_NAME}} import main_function

result = main_function("Hello, World!")
```

### `configure_settings(config)`

Configure global settings.

**Parameters:**
- `config` (dict): Configuration dictionary to merge with defaults

**Example:**
```python
from {{MODULE_NAME}} import configure_settings

configure_settings({
    "setting1": "value1",
    "debug": True
})
```

### `get_settings()`

Get current configuration settings.

**Returns:**
- Current configuration dictionary

**Example:**
```python
from {{MODULE_NAME}} import get_settings

current_config = get_settings()
```

## Utility Functions

### `utility_function(data)`

A utility function that processes data.

**Parameters:**
- `data`: Input data to process

**Returns:**
- Processed string representation

### `helper_function(items, transform=False)`

Helper function to process a list of items.

**Parameters:**
- `items` (list): List of items to process
- `transform` (bool): Whether to apply transformation

**Returns:**
- Processed list of items

## Exceptions

### `{{MODULE_NAME}}Error`

Base exception for {{PROJECT_NAME}}.

### `ConfigurationError`

Raised when there's a configuration error.

### `ProcessingError`

Raised when processing fails.

## Configuration Options

The following configuration options are available:

- `setting1`: Description of setting 1
- `setting2`: Description of setting 2  
- `debug`: Enable debug mode (boolean)
