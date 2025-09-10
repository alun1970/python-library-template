# Python Project Template

A comprehensive template for Python projects based on modern best practices and tooling.

## Features

- 🏗️ Modern Python project structure with `src/` layout
- 📦 `pyproject.toml` configuration for packaging and tools
- 🧪 Test suite with `pytest` and `conftest.py`
- 🎨 Code formatting with `black` and `ruff`
- 🔍 Type checking with `mypy`
- 📋 Comprehensive Makefile for development tasks
- 🚀 GitHub Actions CI/CD pipeline
- 📚 Documentation templates
- 🔧 Example configurations and usage
- 🤖 GitHub Copilot integration

## Project Structure

```
{{PROJECT_NAME}}/
├── src/
│   └── {{MODULE_NAME}}/
│       ├── __init__.py
│       ├── core.py
│       ├── config.py
│       ├── utils.py
│       └── py.typed
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_{{MODULE_NAME}}.py
├── examples/
│   ├── basic_usage.py
│   └── advanced_usage.py
├── docs/
│   ├── API.md
│   └── USAGE.md
├── .github/
│   └── workflows/
│       └── ci.yml
├── pyproject.toml
├── Makefile
├── README.md
├── LICENSE
├── CHANGELOG.md
├── requirements-dev.txt
├── .gitignore
└── .copilot-instructions.md
```

## Quick Start

### Option 1: Using the Setup Script (Recommended)

1. Copy this template directory to your desired location
2. Run the setup script:
   ```bash
   python setup_project.py
   ```
3. Follow the prompts to configure your new project
4. The script will automatically replace template variables and set up your project

### Option 2: Manual Setup

1. Copy this template directory
2. Rename it to your project name
3. Replace all template variables throughout the codebase:
   - `{{PROJECT_NAME}}` - Your project name (e.g., "my-awesome-project")
   - `{{MODULE_NAME}}` - Your Python module name (e.g., "my_awesome_project")
   - `{{PROJECT_DESCRIPTION}}` - Brief description of your project
   - `{{AUTHOR_NAME}}` - Your name
   - `{{AUTHOR_EMAIL}}` - Your email address
   - `{{GITHUB_USERNAME}}` - Your GitHub username
   - `{{MAIN_CLASS}}` - Main class name (e.g., "MyAwesomeProject")

4. Rename the module directory: `src/{{MODULE_NAME}}/` → `src/your_module_name/`
5. Update test files accordingly

## Development Setup

After creating your project:

```bash
# Navigate to your project
cd your-project-name

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"

# Run tests to verify setup
make test

# Run full QA suite
make qa
```

## Available Make Commands

- `make help` - Show all available commands
- `make test` - Run test suite
- `make lint` - Run linting (ruff)
- `make format` - Format code (black)
- `make typecheck` - Run type checking (mypy)
- `make qa` - Run full quality assurance (test + lint + typecheck)
- `make build` - Build package
- `make clean` - Clean build artifacts
- `make install` - Install package in development mode

## Template Variables

When setting up a new project, replace these template variables:

| Variable | Description | Example |
|----------|-------------|---------|
| `{{PROJECT_NAME}}` | Project name | "my-awesome-project" |
| `{{MODULE_NAME}}` | Python module name | "my_awesome_project" |
| `{{PROJECT_DESCRIPTION}}` | Project description | "An awesome Python project" |
| `{{AUTHOR_NAME}}` | Author name | "John Doe" |
| `{{AUTHOR_EMAIL}}` | Author email | "john@example.com" |
| `{{GITHUB_USERNAME}}` | GitHub username | "johndoe" |
| `{{MAIN_CLASS}}` | Main class name | "MyAwesomeProject" |

## Included Tools and Configurations

### Testing
- **pytest**: Modern testing framework
- **conftest.py**: Shared test fixtures and configuration
- Test coverage reporting

### Code Quality
- **black**: Code formatter
- **ruff**: Fast linter (replaces flake8, isort, etc.)
- **mypy**: Static type checker
- **py.typed**: Marks package as type-hinted

### CI/CD
- **GitHub Actions**: Automated testing on multiple Python versions
- **Matrix testing**: Python 3.8, 3.9, 3.10, 3.11, 3.12
- **Multi-OS testing**: Ubuntu, Windows, macOS

### Documentation
- API documentation template
- Usage examples
- Changelog template
- Comprehensive README structure

### Development Tools
- **Makefile**: Common development tasks
- **pyproject.toml**: Modern Python project configuration
- **requirements-dev.txt**: Development dependencies
- **.gitignore**: Comprehensive Python gitignore
- **.copilot-instructions.md**: GitHub Copilot integration

## GitHub Copilot Integration

This template includes GitHub Copilot integration through `.copilot-instructions.md`. This helps Copilot understand your project structure and coding patterns.

## Best Practices Included

1. **Src Layout**: Modern Python project structure
2. **Type Hints**: Full type annotation support
3. **Testing**: Comprehensive test setup with fixtures
4. **Documentation**: API docs and usage examples
5. **CI/CD**: Automated testing and quality checks
6. **Code Quality**: Consistent formatting and linting
7. **Packaging**: Modern Python packaging with pyproject.toml

## License

This template is provided as-is. Update the LICENSE file with your preferred license when creating a new project.

## Contributing

When using this template:

1. Update all template variables
2. Customize the project structure as needed
3. Add your specific dependencies to `pyproject.toml`
4. Update documentation with your project details
5. Configure CI/CD for your specific needs

---

Happy coding! 🚀
