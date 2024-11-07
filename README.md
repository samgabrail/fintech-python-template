# Fintech Python Template

## Development Setup

1. Install Python 3.10 or higher
2. Install pipenv:
   ```bash
   pip install pipenv
   ```

3. Install dependencies:
   ```bash
   # Install all dependencies (including dev)
   pipenv install --dev
   
   # Activate the virtual environment
   pipenv shell
   ```

## Development Commands

### Testing

```bash
# Run tests
pipenv run test

# Run tests with coverage
pipenv run test-cov
```

### Code Quality
```bash
# Format code and sort imports
pipenv run fix

# Check code quality (format, lint, type check)
pipenv run check

# Individual checks
pipenv run format-check  # Check code formatting
pipenv run sort-check   # Check import sorting
pipenv run lint         # Run flake8
pipenv run typecheck    # Run mypy
```

## Project Structure
```
fintech-python-template/
├── src/                 # Source code
│   └── fintech/        # Main package
├── tests/              # Test files
├── notebooks/          # Jupyter notebooks
├── Pipfile             # Dependencies and dev tools
├── pyproject.toml      # Build config and tool settings
└── ...
```