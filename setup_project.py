#!/usr/bin/env python3
"""
Template setup script for creating new Python projects.

This script replaces template variables with actual values and sets up a new project.
"""

import os
import re
import shutil
import sys
from email.utils import parseaddr
from pathlib import Path


def is_valid_email(email: str) -> bool:
    """
    Validate email address format using basic regex and parseaddr.
    This follows RFC 5322 standards more closely than simple regex.
    """
    if not email or "@" not in email:
        return False

    # Use parseaddr to parse the email
    parsed_name, parsed_email = parseaddr(email)

    # Basic validation: must have @ symbol and valid structure
    if not parsed_email or "@" not in parsed_email:
        return False

    # Basic regex for email validation (simplified but covers most cases)
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    return bool(re.match(email_pattern, parsed_email))


def replace_in_file(file_path: Path, replacements: dict):
    """Replace template variables in a file."""
    try:
        content = file_path.read_text(encoding="utf-8")
        for template_var, replacement in replacements.items():
            content = content.replace(template_var, replacement)
        file_path.write_text(content, encoding="utf-8")
    except Exception as e:
        print(f"Warning: Could not process {file_path}: {e}")


def rename_paths(base_path: Path, replacements: dict):
    """Rename files and directories that contain template variables."""
    for root, dirs, files in os.walk(base_path, topdown=False):
        root_path = Path(root)

        # Rename files
        for file in files:
            old_file_path = root_path / file
            new_file_name = file
            for template_var, replacement in replacements.items():
                new_file_name = new_file_name.replace(template_var, replacement)

            if new_file_name != file:
                new_file_path = root_path / new_file_name
                old_file_path.rename(new_file_path)

        # Rename directories
        for dir_name in dirs:
            old_dir_path = root_path / dir_name
            new_dir_name = dir_name
            for template_var, replacement in replacements.items():
                new_dir_name = new_dir_name.replace(template_var, replacement)

            if new_dir_name != dir_name:
                new_dir_path = root_path / new_dir_name
                old_dir_path.rename(new_dir_path)


def setup_project():
    """Setup a new project from the template."""
    print("🚀 Python Project Template Setup")
    print("=" * 40)

    # Get project information
    while True:
        project_name = input("Project name (e.g., my-awesome-project): ").strip()
        if not project_name:
            print("❌ Project name is required!")
            continue

        # Validate PEP 508 identifier (letters, digits, hyphens, periods, underscores)
        if not re.match(
            r"^[a-zA-Z0-9][a-zA-Z0-9._-]*[a-zA-Z0-9]$|^[a-zA-Z0-9]$", project_name
        ):
            print("❌ Project name must be a valid PEP 508 identifier:")
            print("   - Start and end with letters/digits")
            print(
                "   - Can contain letters, digits, hyphens (-), periods (.), underscores (_)"
            )
            print("   - No spaces or other special characters")
            continue
        break

    # Derive module name from project name
    module_name = re.sub(r"[^a-zA-Z0-9]", "_", project_name).lower()
    module_name = re.sub(r"_+", "_", module_name).strip("_")

    project_description = input("Project description: ").strip()
    if not project_description:
        project_description = f"A Python project: {project_name}"

    author_name = input("Author name: ").strip()
    if not author_name:
        author_name = "Your Name"

    # Get and validate author email
    while True:
        author_email = input("Author email: ").strip()
        if not author_email:
            author_email = "your.email@example.com"
            break

        if is_valid_email(author_email):
            break
        else:
            print("❌ Please enter a valid email address (e.g., user@example.com)")
            continue

    github_username = input("GitHub username: ").strip()
    if not github_username:
        github_username = "yourusername"

    # Derive main class name
    main_class = "".join(word.capitalize() for word in module_name.split("_"))
    if not main_class:
        main_class = "MainClass"

    # Create replacements dictionary
    replacements = {
        "{{PROJECT_NAME}}": project_name,
        "{{MODULE_NAME}}": module_name,
        "{{PROJECT_DESCRIPTION}}": project_description,
        "{{AUTHOR_NAME}}": author_name,
        "{{AUTHOR_EMAIL}}": author_email,
        "{{GITHUB_USERNAME}}": github_username,
        "{{MAIN_CLASS}}": main_class,
    }

    # Ensure the src/module_name directory is created, not a nested project
    def fix_src_layout(target_dir, module_name):
        src_dir = target_dir / "src"
        template_src = Path(__file__).parent / "src" / "{{MODULE_NAME}}"
        new_module_dir = src_dir / module_name
        if not new_module_dir.exists():
            new_module_dir.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(template_src, new_module_dir)
            # Remove the old template module dir if it exists
            old_template_dir = src_dir / "{{MODULE_NAME}}"
            if old_template_dir.exists():
                shutil.rmtree(old_template_dir)

    # Show summary
    print("\n📋 Project Summary:")
    print(f"   Project Name: {project_name}")
    print(f"   Module Name: {module_name}")
    print(f"   Main Class: {main_class}")
    print(f"   Description: {project_description}")
    print(f"   Author: {author_name} <{author_email}>")
    print(f"   GitHub: {github_username}")

    confirm = input("\n✅ Continue with setup? (y/N): ").strip().lower()
    if confirm not in ["y", "yes"]:
        print("❌ Setup cancelled.")
        sys.exit(0)

    # Get target directory
    target_dir_input = input(
        f"\n📁 Target directory (default: ./{project_name}): "
    ).strip()
    if not target_dir_input:
        target_dir = Path(f"./{project_name}")
    else:
        target_dir = Path(target_dir_input)

    # Prevent accidental overwrite in current directory
    if target_dir.resolve() == Path(".").resolve():
        print("⚠️  You are about to run the template setup in the current directory!")
        print("   This may overwrite template files and is NOT recommended.")
        confirm_current = (
            input(
                "Are you sure you want to continue in the current directory? (Type 'yes' to confirm): "
            )
            .strip()
            .lower()
        )
        if confirm_current != "yes":
            print(
                "❌ Setup cancelled. Please specify a new directory for your project."
            )
            sys.exit(1)

    # Create target directory if it does not exist
    if target_dir.exists() and any(target_dir.iterdir()):
        print(f"❌ Directory {target_dir} already exists and is not empty!")
        sys.exit(1)
    elif not target_dir.exists():
        target_dir.mkdir(parents=True)

    # Copy template to target directory (skip if current directory)
    template_dir = Path(__file__).parent
    if target_dir.resolve() != template_dir.resolve():
        print(f"\n📋 Copying template to {target_dir}...")
        shutil.copytree(
            template_dir,
            target_dir,
            dirs_exist_ok=True,
            ignore=shutil.ignore_patterns("setup_project.py", ".git", "__pycache__"),
        )
    else:
        print("\n📋 Using current directory as project root...")

    # Fix src layout to avoid nested project directories
    fix_src_layout(target_dir, module_name)

    # Rename paths first
    print("🔧 Renaming files and directories...")
    rename_paths(target_dir, replacements)

    # Replace template variables in all files
    print("📝 Replacing template variables...")
    for root, _dirs, files in os.walk(target_dir):
        for file in files:
            file_path = Path(root) / file
            if file_path.suffix in [".py", ".md", ".txt", ".toml", ".yml", ".yaml"]:
                replace_in_file(file_path, replacements)

    print(f"\n🎉 Project {project_name} created successfully!")
    print(f"📁 Location: {target_dir.absolute()}")

    # Offer to set up virtual environment and install dependencies
    setup_venv = (
        input("\n� Set up virtual environment and install dependencies? (Y/n): ")
        .strip()
        .lower()
    )
    if setup_venv in ["", "y", "yes"]:
        print("\n🔧 Setting up virtual environment...")
        import subprocess
        import time

        try:
            # Always create a new venv in the target directory, removing any existing one
            venv_path = target_dir / "venv"
            if venv_path.exists():
                print("   Removing existing venv...")
                shutil.rmtree(venv_path)
            print("   Creating virtual environment...")
            subprocess.run(
                [sys.executable, "-m", "venv", "venv"], cwd=target_dir, check=True
            )
            time.sleep(1)
            # Determine the python executable in the venv
            if sys.platform == "win32":
                venv_python = target_dir / "venv" / "Scripts" / "python.exe"
                activate_cmd = "venv\\Scripts\\activate"
            else:
                venv_python = target_dir / "venv" / "bin" / "python"
                activate_cmd = "source venv/bin/activate"
            # Check if venv python exists
            if not venv_python.exists():
                raise FileNotFoundError(
                    f"Virtual environment Python not found at {venv_python}"
                )
            # Upgrade pip and install the package in development mode
            print("   Upgrading pip and installing dependencies...")
            subprocess.run(
                [str(venv_python), "-m", "pip", "install", "--upgrade", "pip"],
                cwd=target_dir,
                check=True,
            )
            subprocess.run(
                [str(venv_python), "-m", "pip", "install", "-e", ".[dev]"],
                cwd=target_dir,
                check=True,
            )
            print("✅ Virtual environment setup complete!")
            # Test hello world functionality
            test_hello = input("\n🧪 Run Hello World test? (Y/n): ").strip().lower()
            if test_hello in ["", "y", "yes"]:
                print("   Running Hello World test...")
                result = subprocess.run(
                    [str(venv_python), "test_hello_world.py"],
                    cwd=target_dir,
                    capture_output=True,
                    text=True,
                )
                if result.returncode == 0:
                    print("✅ Hello World test passed!")
                else:
                    print("❌ Hello World test failed:")
                    print(result.stderr)
            print("\n�🚀 Next steps:")
            print(f"   cd {target_dir}")
            print(f"   {activate_cmd}")
            print("   make demo-hello  # Run Hello World demo")
            print("   make test        # Run full test suite")
            print("   make qa          # Run quality assurance")
        except subprocess.CalledProcessError as e:
            print(f"❌ Error setting up virtual environment: {e}")
            print("You can set it up manually using the commands below.")
            print("\n🚀 Manual setup:")
            print(f"   cd {target_dir}")
            print("   python -m venv venv")
            print(f"   {activate_cmd}")
            print('   pip install -e ".[dev]"')
            print("   make test-hello")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            print("Please set up the environment manually.")
    else:
        print("\n🚀 Manual setup steps:")
        print(f"   cd {target_dir}")
        print("   python -m venv venv")
        if sys.platform == "win32":
            print("   venv\\Scripts\\activate")
        else:
            print("   source venv/bin/activate")
        print('   pip install -e ".[dev]"')
        print("   make test-hello")
    print("\n💡 See README.md for more information.")


if __name__ == "__main__":
    setup_project()
