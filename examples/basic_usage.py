#!/usr/bin/env python3
"""
Basic usage example for {{PROJECT_NAME}}.

This example demonstrates the basic functionality of the package.
"""

import sys
from pathlib import Path

# Add the src directory to the path for direct imports during development
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

# from {{MODULE_NAME}} import {{MAIN_CLASS}}, main_function, hello_world


def main():
    """Demonstrate basic usage."""
    print("=== {{PROJECT_NAME}} Basic Usage Example ===\n")

    # Example 1: Hello World functionality
    print("1. Hello World examples:")
    # print(f"Simple greeting: {hello_world()}")
    # print(f"Personal greeting: {hello_world('Developer')}")
    # print()

    # Example 2: Using the main function
    print("2. Using main function:")
    # result = main_function("Hello, World!")
    # print(f"Result: {result}\n")

    # Example 3: Using the main class
    print("3. Using main class:")
    # instance = {{MAIN_CLASS}}()
    # print(f"Hello from class: {instance.hello_world('User')}")
    # result = instance.process("Sample data")
    # print(f"Process result: {result}\n")

    # Example 4: With configuration
    print("4. With custom configuration:")
    # config = {"setting1": "custom_value", "debug": True}
    # instance = {{MAIN_CLASS}}(config=config)
    # print(f"Configured greeting: {instance.hello_world('Admin')}")
    # result = instance.process("Configured processing")
    # print(f"Process result: {result}\n")

    print("=== Example Complete ===")


if __name__ == "__main__":
    main()
