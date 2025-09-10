#!/usr/bin/env python3
"""
Hello World example for {{PROJECT_NAME}}.

This script demonstrates basic hello world functionality.
"""

import sys
from pathlib import Path

# Add the src directory to the path for importing
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from {{MODULE_NAME}} import {{MAIN_CLASS}}, hello_world  # noqa: E402


def main():
    """Main function demonstrating hello world functionality."""
    print("🌟 {{PROJECT_NAME}} - Hello World Demo")
    print("=" * 50)

    # Using the standalone hello_world function
    print("\n1. Standalone function:")
    print(f"   {hello_world()}")
    print(f"   {hello_world('Alice')}")
    print(f"   {hello_world('Developer')}")

    # Using the class method
    print("\n2. Class method:")
    instance = {{MAIN_CLASS}}()
    print(f"   {instance.hello_world()}")
    print(f"   {instance.hello_world('Bob')}")
    print(f"   {instance.hello_world('World')}")

    # With configuration
    print("\n3. With configuration:")
    config = {"greeting_style": "friendly"}
    configured_instance = {{MAIN_CLASS}}(config)
    print(f"   {configured_instance.hello_world('Team')}")

    print("\n✅ Hello World demo completed!")


if __name__ == "__main__":
    main()
