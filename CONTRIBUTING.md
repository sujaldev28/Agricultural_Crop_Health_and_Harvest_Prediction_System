# Contributing to Agricultural Crop Health System

Thank you for your interest in contributing to our project!

## Development Workflow

1. Fork the repository and create your branch from `main`.
2. Install developer tooling dependencies:
   ```bash
   pip install -r requirements.txt
   pre-commit install
   ```
3. Implement your changes, adding tests as appropriate.
4. Ensure all checks pass:
   ```bash
   pytest
   ruff check .
   black --check .
   mypy src/
   ```
5. Submit a Pull Request.

## Code Style

We follow PEP8 and use the following tools:
- **Black** for formatting.
- **Ruff** for linting.
- **MyPy** for strict type verification.
