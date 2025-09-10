#!/usr/bin/env python3
"""
Test runner for {{PROJECT_NAME}} hello world functionality.

This script provides a quick way to test the hello world features
without running the full test suite.
"""

import sys
from pathlib import Path

# Add the src directory to the path for importing
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))


def test_hello_world_functions():
    """Test the hello world functionality."""
    print("🧪 Testing Hello World Functionality")
    print("=" * 50)

    try:
        # Import after adding to path
        from {{MODULE_NAME}} import {{MAIN_CLASS}}, hello_world

        # Test standalone function
        print("\n1. Testing standalone hello_world function:")

        # Test without name
        result1 = hello_world()
        print(f"   hello_world() → {result1}")
        assert "Hello, World!" in result1
        assert "{{PROJECT_NAME}}" in result1
        print("   ✅ Test passed: hello_world() without name")

        # Test with name
        result2 = hello_world("Tester")
        print(f"   hello_world('Tester') → {result2}")
        assert "Hello, Tester!" in result2
        assert "{{PROJECT_NAME}}" in result2
        print("   ✅ Test passed: hello_world() with name")

        # Test class method
        print("\n2. Testing {{MAIN_CLASS}}.hello_world method:")

        instance = {{MAIN_CLASS}}()

        # Test without name
        result3 = instance.hello_world()
        print(f"   instance.hello_world() → {result3}")
        assert "Hello, World!" in result3
        assert "{{PROJECT_NAME}}" in result3
        print("   ✅ Test passed: class method without name")

        # Test with name
        result4 = instance.hello_world("Developer")
        print(f"   instance.hello_world('Developer') → {result4}")
        assert "Hello, Developer!" in result4
        assert "{{PROJECT_NAME}}" in result4
        print("   ✅ Test passed: class method with name")

        # Test with configuration
        print("\n3. Testing with configuration:")
        config = {"greeting_style": "formal"}
        configured_instance = {{MAIN_CLASS}}(config)
        result5 = configured_instance.hello_world("User")
        print(f"   configured_instance.hello_world('User') → {result5}")
        assert "Hello, User!" in result5
        assert "{{PROJECT_NAME}}" in result5
        print("   ✅ Test passed: class method with configuration")

        print("\n🎉 All Hello World tests passed!")
        return True

    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("   Make sure you've set up the template correctly.")
        return False
    except AssertionError as e:
        print(f"❌ Test assertion failed: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False


def test_edge_cases():
    """Test edge cases for hello world functionality."""
    print("\n🔍 Testing Edge Cases")
    print("-" * 30)

    try:
        from {{MODULE_NAME}} import hello_world

        # Test with empty string
        result1 = hello_world("")
        print(f"   hello_world('') → {result1}")
        # Empty string should behave like None
        assert "Hello, World!" in result1
        print("   ✅ Test passed: empty string")

        # Test with None explicitly
        result2 = hello_world(None)
        print(f"   hello_world(None) → {result2}")
        assert "Hello, World!" in result2
        print("   ✅ Test passed: None value")

        # Test with special characters
        result3 = hello_world("José María")
        print(f"   hello_world('José María') → {result3}")
        assert "Hello, José María!" in result3
        print("   ✅ Test passed: special characters")

        # Test with numbers
        result4 = hello_world("User123")
        print(f"   hello_world('User123') → {result4}")
        assert "Hello, User123!" in result4
        print("   ✅ Test passed: alphanumeric name")

        print("\n🎉 All edge case tests passed!")
        return True

    except Exception as e:
        print(f"❌ Edge case test failed: {e}")
        return False


def main():
    """Run all hello world tests."""
    print("🚀 {{PROJECT_NAME}} - Hello World Test Runner")
    print("=" * 60)

    # Run basic tests
    basic_tests_passed = test_hello_world_functions()

    # Run edge case tests
    edge_tests_passed = test_edge_cases()

    # Summary
    print("\n📊 Test Summary:")
    print(f"   Basic tests: {'✅ PASSED' if basic_tests_passed else '❌ FAILED'}")
    print(f"   Edge cases:  {'✅ PASSED' if edge_tests_passed else '❌ FAILED'}")

    if basic_tests_passed and edge_tests_passed:
        print("\n🎉 All tests completed successfully!")
        print("✨ Hello World functionality is working correctly!")
        return 0
    else:
        print("\n❌ Some tests failed!")
        print("🔧 Please check the implementation and try again.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
