# Python Project Template

�� **A comprehensive Python project template with modern tooling and Hello World functionality**

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Template](https://img.shields.io/badge/template-ready-brightgreen.svg)

## ⚡ Quick Start

### Option 1: GitHub Actions (One-Click Setup) ✨
1. Go to **Actions** tab in this repository
2. Click **"🚀 Generate Python Project"** workflow
3. Click **"Run workflow"** button
4. Fill in your project details and click **"Run workflow"**
5. Your new repository will be created automatically!

> **Note**: Repository owner needs to set up a `PERSONAL_ACCESS_TOKEN` secret first (see setup instructions below)

### Option 2: Use GitHub Template (Traditional)
1. Click **"Use this template"** button above
2. Create your new repository  
3. Clone your new repository
4. Run the setup script:
   ```bash
   python setup_project.py
   ```

### Option 3: Manual Setup
```bash
# Clone this template
git clone https://github.com/alun1970/python-project-template.git my-new-project
cd my-new-project

# Run setup script
python setup_project.py
```

## 🎯 What You Get

- **🏗️ Modern Structure**: `src/` layout with proper packaging
- **📦 Build System**: `pyproject.toml` configuration  
- **🧪 Testing**: pytest with comprehensive test setup
- **🎨 Code Quality**: black, ruff, mypy integration
- **📋 Development**: Comprehensive Makefile
- **🚀 CI/CD**: GitHub Actions workflow
- **📚 Documentation**: API docs, usage examples
- **🤖 AI Ready**: GitHub Copilot integration
- **👋 Example Code**: Hello World functionality with tests

## 🛠️ Features

### Ready-to-Use Development Environment
- Virtual environment setup
- Dependency management  
- Code formatting and linting
- Type checking
- Automated testing

### Make Commands
```bash
make test-hello    # Quick Hello World test
make demo-hello    # Hello World demo
make test          # Run test suite
make qa            # Full quality assurance
make format        # Format code
make build         # Build package
```

### Template Variables
The setup script replaces these automatically:
- `{{PROJECT_NAME}}` → Your project name
- `{{MODULE_NAME}}` → Python module name
- `{{AUTHOR_NAME}}` → Your name
- `{{AUTHOR_EMAIL}}` → Your email  
- `{{GITHUB_USERNAME}}` → Your GitHub username

## 📁 Project Structure

```
your-project/
├── src/your_module/          # Source code
├── tests/                    # Test suite
├── examples/                 # Usage examples
├── docs/                     # Documentation
├── .github/workflows/        # CI/CD
├── pyproject.toml           # Project configuration
├── Makefile                 # Development commands
└── README.md                # Project documentation
```

## 🚀 Getting Started

### For Repository Owners: GitHub Actions Setup

To enable the one-click project generation:

1. **Create a Personal Access Token**:
   - Go to [GitHub Settings > Personal Access Tokens](https://github.com/settings/tokens)
   - Click "Generate new token (classic)"
   - Select scopes: `repo` (Full control of private repositories)
   - Copy the generated token

2. **Add the token as a repository secret**:
   - Go to your repository **Settings**
   - Navigate to **Secrets and variables** > **Actions**
   - Click **"New repository secret"**
   - Name: `PERSONAL_ACCESS_TOKEN`
   - Value: Paste your token
   - Click **"Add secret"**

### For Project Generation:

1. **Use this template** to create your repository
2. **Clone** your new repository
3. **Run setup script**: `python setup_project.py`
4. **Activate environment**: `source venv/bin/activate`
5. **Test**: `make test-hello`
6. **Start coding!**

## 📖 Documentation

- **Template Setup**: See `TEMPLATE_README.md`
- **Development**: Check the generated `README.md` in your new project
- **API Documentation**: `docs/API.md`
- **Usage Examples**: `examples/` directory

## 🤝 Contributing

This template is designed to be a solid starting point. Feel free to:
- Fork and customize for your needs
- Submit improvements via pull requests
- Report issues or suggestions

## 📄 License

MIT License - see LICENSE file for details.

---

**Happy coding!** 🎉
