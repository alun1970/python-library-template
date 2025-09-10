# {{PROJECT_NAME}} - Development Makefile
PYTHON := python
PIP := pip
SRC_DIR := src
TESTS_DIR := tests
EXAMPLES_DIR := examples
VENV_DIR := venv
DIST_DIR := dist

# Check if venv exists and use it, otherwise use system python
ifeq ($(OS),Windows_NT)
    VENV_PYTHON := $(if $(wildcard $(VENV_DIR)/Scripts/python.exe),$(VENV_DIR)/Scripts/python.exe,$(PYTHON))
    VENV_ACTIVATE := $(if $(wildcard $(VENV_DIR)/Scripts/activate.bat),$(VENV_DIR)/Scripts/activate.bat &&,)
else
    VENV_PYTHON := $(if $(wildcard $(VENV_DIR)/bin/python),$(VENV_DIR)/bin/python,$(PYTHON))
    VENV_ACTIVATE := $(if $(wildcard $(VENV_DIR)/bin/activate),. $(VENV_DIR)/bin/activate &&,)
endif

.DEFAULT_GOAL := help

.PHONY: setup
setup: ## Setup development environment
	@echo "🚀 Setting up development environment..."
	@if [ ! -d "$(VENV_DIR)" ]; then $(PYTHON) -m venv $(VENV_DIR); fi
	@. $(VENV_DIR)/bin/activate && $(PIP) install -e ".[dev]"
	@echo "✅ Development environment ready!"

.PHONY: test
test: ## Run tests
	@echo "🧪 Running tests..."
	@. $(VENV_DIR)/bin/activate && $(PYTHON) -m pytest $(TESTS_DIR) -v

.PHONY: test-hello
test-hello: ## Run hello world test
	@echo "👋 Testing Hello World functionality..."
	@$(VENV_PYTHON) test_hello_world.py

.PHONY: demo-hello
demo-hello: ## Run hello world demo
	@echo "🌟 Running Hello World demo..."
	@$(VENV_PYTHON) $(EXAMPLES_DIR)/hello_world.py

.PHONY: test-coverage
test-coverage: ## Run tests with coverage
	@echo "🧪 Running tests with coverage..."
	@. $(VENV_DIR)/bin/activate && $(PYTHON) -m pytest $(TESTS_DIR) --cov=$(SRC_DIR) --cov-report=html --cov-report=term -v

.PHONY: lint
lint: ## Run linting
	@echo "🔍 Running linting..."
	@. $(VENV_DIR)/bin/activate && $(PYTHON) -m ruff check .

.PHONY: format
format: ## Format code
	@echo "🎨 Formatting code..."
	@. $(VENV_DIR)/bin/activate && $(PYTHON) -m black .
	@. $(VENV_DIR)/bin/activate && $(PYTHON) -m isort .

.PHONY: format-check
format-check: ## Check code formatting
	@echo "🎨 Checking code formatting..."
	@. $(VENV_DIR)/bin/activate && $(PYTHON) -m black --check .
	@. $(VENV_DIR)/bin/activate && $(PYTHON) -m isort --check-only .

.PHONY: typecheck
typecheck: ## Run type checking
	@echo "🔎 Running type checking..."
	@. $(VENV_DIR)/bin/activate && $(PYTHON) -m mypy $(SRC_DIR)

.PHONY: qa
qa: ## Run quality assurance
	@echo "🎯 Running QA checks..."
	@. $(VENV_DIR)/bin/activate && $(PYTHON) -m pytest $(TESTS_DIR) -v
	@. $(VENV_DIR)/bin/activate && $(PYTHON) -m mypy $(SRC_DIR)
	@. $(VENV_DIR)/bin/activate && $(PYTHON) -m ruff check .
	@. $(VENV_DIR)/bin/activate && $(PYTHON) -m black --check .
	@echo "✅ All QA checks passed!"

.PHONY: build
build: ## Build packages
	@echo "📦 Building packages..."
	@rm -rf $(DIST_DIR)/ build/ *.egg-info/
	@. $(VENV_DIR)/bin/activate && $(PYTHON) -m build
	@echo "✅ Build complete!"

.PHONY: publish-test
publish-test: build ## Publish to TestPyPI
	@echo "📤 Publishing to TestPyPI..."
	@. $(VENV_DIR)/bin/activate && $(PYTHON) -m twine upload --repository testpypi $(DIST_DIR)/*

.PHONY: publish
publish: build ## Publish to PyPI
	@echo "📤 Publishing to PyPI..."
	@. $(VENV_DIR)/bin/activate && $(PYTHON) -m twine upload $(DIST_DIR)/*

.PHONY: install-dev
install-dev: ## Install in development mode
	@echo "📥 Installing in development mode..."
	@. $(VENV_DIR)/bin/activate && $(PIP) install -e ".[dev]"

.PHONY: clean
clean: ## Clean artifacts
	@echo "🧹 Cleaning..."
	@rm -rf $(DIST_DIR)/ build/ *.egg-info/ .pytest_cache/ .mypy_cache/ .ruff_cache/ htmlcov/
	@find . -name "*.pyc" -delete
	@find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true

.PHONY: docs
docs: ## Generate documentation
	@echo "📚 Generating documentation..."
	@. $(VENV_DIR)/bin/activate && cd docs && make html

.PHONY: help
help: ## Show help
	@echo "{{PROJECT_NAME}} - Development Commands"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "%-15s %s\n", $$1, $$2}'
