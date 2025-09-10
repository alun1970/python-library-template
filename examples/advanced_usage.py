#!/usr/bin/env python3
"""
Advanced usage example for {{PROJECT_NAME}}.

This example demonstrates advanced features and configuration options.
"""

import sys
from pathlib import Path

# Add the src directory to the path for direct imports during development
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

# from {{MODULE_NAME}} import (
#     {{MAIN_CLASS}},
#     configure_settings,
#     get_settings,
#     utility_function,
#     helper_function,
# )


def main():
    """Demonstrate advanced usage."""
    print("=== {{PROJECT_NAME}} Advanced Usage Example ===\n")

    # Example 1: Global configuration
    print("1. Global configuration:")
    # configure_settings({
    #     "setting1": "advanced_value",
    #     "setting2": "another_value",
    #     "debug": True
    # })
    # current_settings = get_settings()
    # print(f"Current settings: {current_settings}\n")

    # Example 2: Advanced processing
    print("2. Advanced processing:")
    # instance = {{MAIN_CLASS}}()
    # options = {
    #     "mode": "advanced",
    #     "transform": True,
    #     "output_format": "json"
    # }
    # result = instance.advanced_process("Complex data", options)
    # print(f"Advanced result: {result}\n")

    # Example 3: Using utilities
    print("3. Using utility functions:")
    # data = ["item1", "item2", "item3"]
    # processed_data = helper_function(data, transform=True)
    # print(f"Processed data: {processed_data}")
    #
    # utility_result = utility_function(processed_data)
    # print(f"Utility result: {utility_result}\n")

    # Example 4: Error handling
    print("4. Error handling:")
    # try:
    #     # This would raise an exception in a real implementation
    #     pass
    # except Exception as e:
    #     print(f"Caught exception: {e}\n")

    # Example 5: Batch processing
    print("5. Batch processing:")
    # items_to_process = ["data1", "data2", "data3", "data4"]
    # instance = {{MAIN_CLASS}}()
    #
    # results = []
    # for i, item in enumerate(items_to_process):
    #     result = instance.process(f"{item}_batch_{i}")
    #     results.append(result)
    #
    # print(f"Batch results: {results}\n")

    print("=== Advanced Example Complete ===")


if __name__ == "__main__":
    main()
