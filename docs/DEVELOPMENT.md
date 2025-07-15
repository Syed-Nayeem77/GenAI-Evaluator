# Development Guide

## Setup
1. Clone the repository
2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   .\venv\Scripts\activate  # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

## Coding Standards
- Follow PEP 8 style guide
- Use type hints for all function signatures
- Keep functions small and focused
- Write docstrings for all public methods

## Testing
Run all tests:
```bash
pytest tests/
```

Run with coverage:
```bash
pytest --cov=src tests/
```

## Linting
Check code quality:
```bash
make lint
```

Auto-format code:
```bash
make format
```

## Version Control
- Create feature branches from `main`
- Use descriptive commit messages
- Open pull requests for code review
