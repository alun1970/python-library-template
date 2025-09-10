#!/usr/bin/env python3
"""
Template setup script for creating new Python projects.

This script replaces template variables with actual values and sets up a new project.
"""

import os
import re
import shutil
import sys
from pathlib import Path


def replace_in_file(file_path: Path, replacements: dict):
    """Replace template variables in a file."""
    try:
        content = file_path.read_text(encoding='utf-8')
        for template_var, replacement in replacements.items():
            content = content.replace(template_var, replacement)
        file_path.write_text(content, encoding='utf-8')
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
    project_name = input("Project name (e.g., my-awesome-project): ").strip()
    if not project_name:
        print("❌ Project name is required!")
        sys.exit(1)
    
    # Derive module name from project name
    module_name = re.sub(r'[^a-zA-Z0-9]', '_', project_name).lower()
    module_name = re.sub(r'_+', '_', module_name).strip('_')
    
    project_description = input(f"Project description: ").strip()
    if not project_description:
        project_description = f"A Python project: {project_name}"
    
    author_name = input("Author name: ").strip()
    if not author_name:
        author_name = "Your Name"
    
    author_email = input("Author email: ").strip()
    if not author_email:
        author_email = "your.email@example.com"
    
    github_username = input("GitHub username: ").strip()
    if not github_username:
        github_username = "yourusername"
    
    # Derive main class name
    main_class = ''.join(word.capitalize() for word in module_name.split('_'))
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
    
    # Show summary
    print("\n📋 Project Summary:")
    print(f"   Project Name: {project_name}")
    print(f"   Module Name: {module_name}")
    print(f"   Main Class: {main_class}")
    print(f"   Description: {project_description}")
    print(f"   Author: {author_name} <{author_email}>")
    print(f"   GitHub: {github_username}")
    
    confirm = input("\n✅ Continue with setup? (y/N): ").strip().lower()
    if confirm not in ['y', 'yes']:
        print("❌ Setup cancelled.")
        sys.exit(0)
    
    # Get target directory
    target_dir = Path(input(f"\n📁 Target directory (default: ./{project_name}): ").strip())
    if not target_dir.name:
        target_dir = Path(f"./{project_name}")
    
    # Create target directory
    if target_dir.exists():
        print(f"❌ Directory {target_dir} already exists!")
        sys.exit(1)
    
    # Copy template to target directory
    template_dir = Path(__file__).parent
    print(f"\n📋 Copying template to {target_dir}...")
    shutil.copytree(template_dir, target_dir, ignore=shutil.ignore_patterns('setup_project.py', '.git', '__pycache__'))
    
    # Rename paths first
    print("🔧 Renaming files and directories...")
    rename_paths(target_dir, replacements)
    
    # Replace template variables in all files
    print("📝 Replacing template variables...")
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            file_path = Path(root) / file
            if file_path.suffix in ['.py', '.md', '.txt', '.toml', '.yml', '.yaml']:
                replace_in_file(file_path, replacements)
    
    print(f"\n🎉 Project {project_name} created successfully!")
    print(f"📁 Location: {target_dir.absolute()}")
    
    # Offer to set up virtual environment and install dependencies
    setup_venv = input("\n� Set up virtual environment and install dependencies? (Y/n): ").strip().lower()
    if setup_venv in ['', 'y', 'yes']:
        print("\n🔧 Setting up virtual environment...")
        
        import subprocess
        import sys
        
        try:
            # Create virtual environment
            print("   Creating virtual environment...")
            subprocess.run([sys.executable, "-m", "venv", "venv"], cwd=target_dir, check=True)
            
            # Wait a moment for filesystem to sync
            import time
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
                raise FileNotFoundError(f"Virtual environment Python not found at {venv_python}")
            
            # Install the package in development mode
            print("   Installing dependencies...")
            subprocess.run([str(venv_python), "-m", "pip", "install", "-e", ".[dev]"], cwd=target_dir, check=True)
            
            print("✅ Virtual environment setup complete!")
            
            # Test hello world functionality
            test_hello = input("\n🧪 Run Hello World test? (Y/n): ").strip().lower()
            if test_hello in ['', 'y', 'yes']:
                print("   Running Hello World test...")
                result = subprocess.run([str(venv_python), "test_hello_world.py"], cwd=target_dir, capture_output=True, text=True)
                if result.returncode == 0:
                    print("✅ Hello World test passed!")
                else:
                    print("❌ Hello World test failed:")
                    print(result.stderr)
            
            print(f"\n�🚀 Next steps:")
            print(f"   cd {target_dir}")
            print(f"   {activate_cmd}")
            print("   make demo-hello  # Run Hello World demo")
            print("   make test        # Run full test suite")
            print("   make qa          # Run quality assurance")
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Error setting up virtual environment: {e}")
            print("You can set it up manually using the commands below.")
            print(f"\n🚀 Manual setup:")
            print(f"   cd {target_dir}")
            print("   python -m venv venv")
            print(f"   {activate_cmd}")
            print("   pip install -e \".[dev]\"")
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
        print("   pip install -e \".[dev]\"")
        print("   make test-hello")
    
    print("\n💡 See README.md for more information.")


if __name__ == "__main__":
    setup_project()
