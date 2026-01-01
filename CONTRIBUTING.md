# Contributing to RAGbot

Thank you for your interest in contributing to RAGbot! We welcome contributions from the community and are grateful for your support.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Code Style Guidelines](#code-style-guidelines)
- [Testing](#testing)
- [Documentation](#documentation)
- [Submitting Changes](#submitting-changes)
- [Reporting Bugs](#reporting-bugs)
- [Requesting Features](#requesting-features)

---

## Code of Conduct

This project adheres to the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

---

## How Can I Contribute?

There are many ways to contribute to RAGbot:

- 🐛 **Report bugs** - Help us identify and fix issues
- 💡 **Suggest features** - Share ideas for improvements
- 📝 **Improve documentation** - Help others understand the project
- 🔧 **Submit pull requests** - Contribute code changes
- 🧪 **Write tests** - Improve code coverage and reliability
- 🎨 **Improve UI/UX** - Enhance the user experience
- 📦 **Update dependencies** - Keep the project up-to-date

---

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js** 18+ and npm
- **Python** 3.10+
- **Git**

### Fork and Clone

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:

```bash
git clone https://github.com/YOUR_USERNAME/RAGbot.git
cd RAGbot
```

3. **Add upstream remote**:

```bash
git remote add upstream https://github.com/H0NEYP0T-466/RAGbot.git
```

4. **Install dependencies**:

```bash
# Frontend
npm install

# Backend
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## Development Workflow

### 1. Create a Feature Branch

Always create a new branch for your work:

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

Branch naming conventions:
- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation updates
- `refactor/` - Code refactoring
- `test/` - Test additions or updates
- `chore/` - Maintenance tasks

### 2. Make Your Changes

- Write clean, readable code
- Follow the code style guidelines (see below)
- Add tests for new functionality
- Update documentation as needed
- Commit your changes with clear, descriptive messages

### 3. Keep Your Fork Updated

Regularly sync your fork with the upstream repository:

```bash
git fetch upstream
git checkout main
git merge upstream/main
```

### 4. Push Your Changes

```bash
git push origin feature/your-feature-name
```

### 5. Submit a Pull Request

- Go to your fork on GitHub
- Click "New Pull Request"
- Select your feature branch
- Fill out the PR template completely
- Link any related issues
- Wait for review and address feedback

---

## Code Style Guidelines

### Frontend (TypeScript/React)

- **Linting**: Use ESLint for code quality
  ```bash
  npm run lint
  ```
- **Formatting**: Consistent formatting is enforced by ESLint
- **TypeScript**: Use strict type checking
  - Avoid `any` types when possible
  - Define interfaces for component props
  - Use type inference where appropriate
- **React**:
  - Use functional components with hooks
  - Keep components focused and single-purpose
  - Use meaningful component and variable names
  - Extract reusable logic into custom hooks

### Backend (Python)

- **Style**: Follow PEP 8 style guide
- **Type Hints**: Use type hints for function parameters and return values
- **Docstrings**: Write clear docstrings for all public functions and classes
  ```python
  def function_name(param: str) -> bool:
      """
      Brief description of function.

      Args:
          param: Description of parameter

      Returns:
          Description of return value
      """
      pass
  ```
- **Imports**: Organize imports in the following order:
  1. Standard library imports
  2. Third-party imports
  3. Local application imports
- **Error Handling**: Use proper exception handling
- **Logging**: Use the logging module instead of print statements

### General Guidelines

- **Comments**: Write comments for complex logic, not obvious code
- **Naming**:
  - Use descriptive variable and function names
  - Use `camelCase` for TypeScript/JavaScript
  - Use `snake_case` for Python
- **File Organization**: Keep related code together
- **DRY Principle**: Don't Repeat Yourself - extract common functionality
- **KISS Principle**: Keep It Simple, Stupid - prefer simple solutions

---

## Testing

### Frontend Tests

While the project currently doesn't have extensive test coverage, contributions that include tests are highly valued:

```bash
# Run tests (when available)
npm test
```

### Backend Tests

Ensure your changes don't break existing functionality:

```bash
# Manual testing
python -m app.main
# Test endpoints manually or with curl
```

### Testing Checklist

When submitting a PR, ensure you've tested:

- ✅ Your new feature or fix works as expected
- ✅ Existing features still work correctly
- ✅ Edge cases are handled appropriately
- ✅ Error messages are clear and helpful
- ✅ The application runs without errors in the console

---

## Documentation

Good documentation is crucial. When contributing:

### Code Documentation

- Add docstrings to Python functions and classes
- Add JSDoc comments for complex TypeScript functions
- Update inline comments for complex logic

### README Updates

Update the README.md if your changes:
- Add new features
- Change installation or usage instructions
- Modify API endpoints
- Update dependencies

### Additional Documentation

- Update relevant documentation files (CONTRIBUTING.md, SECURITY.md, etc.)
- Add examples for new features
- Update the folder structure if you add new directories

---

## Submitting Changes

### Pull Request Guidelines

1. **Fill out the PR template completely**
2. **Link related issues** (e.g., "Fixes #123")
3. **Provide a clear description** of what your PR does
4. **Include screenshots** for UI changes
5. **List any breaking changes**
6. **Update documentation** as needed
7. **Ensure CI checks pass** (when available)

### PR Checklist

Before submitting, verify:

- [ ] Code follows the style guidelines
- [ ] Self-review of code completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings introduced
- [ ] Tests added for new features
- [ ] All tests passing
- [ ] Backward compatibility maintained (or breaking changes documented)

### Commit Message Guidelines

Write clear, descriptive commit messages:

```
<type>: <short summary>

<optional detailed description>

<optional footer>
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Test additions or updates
- `chore`: Maintenance tasks
- `perf`: Performance improvements

Examples:
```
feat: add support for PDF document uploads

fix: resolve issue with chat history not scrolling

docs: update installation instructions for Windows
```

---

## Reporting Bugs

### Before Submitting a Bug Report

1. **Check existing issues** to avoid duplicates
2. **Test with the latest version** of the code
3. **Collect relevant information**:
   - Operating system and version
   - Node.js and Python versions
   - Browser and version (for frontend issues)
   - Steps to reproduce the issue
   - Expected vs. actual behavior
   - Error messages and logs

### Submitting a Bug Report

Use the [Bug Report Template](.github/ISSUE_TEMPLATE/bug_report.yml) and include:

- Clear, descriptive title
- Detailed steps to reproduce
- Expected behavior
- Actual behavior
- Screenshots or error logs
- Environment details
- Severity assessment

---

## Requesting Features

We welcome feature suggestions! When requesting a feature:

### Use the Feature Request Template

Use the [Feature Request Template](.github/ISSUE_TEMPLATE/feature_request.yml) and include:

- **Problem statement**: What problem does this solve?
- **Proposed solution**: How should it work?
- **Alternatives considered**: Other approaches you've thought about
- **Additional context**: Any relevant information, mockups, or examples

### Feature Evaluation Criteria

Features will be evaluated based on:

- Alignment with project goals
- Value to users
- Implementation complexity
- Maintenance burden
- Breaking changes required

---

## Development Tips

### Useful Commands

```bash
# Frontend
npm run dev          # Start development server
npm run build        # Build for production
npm run lint         # Run ESLint
npm run preview      # Preview production build

# Backend
python -m app.main   # Start FastAPI server
```

### Debugging

- **Frontend**: Use browser DevTools console
- **Backend**: Check server logs in the terminal
- **Network**: Use browser Network tab to inspect API calls

### Common Issues

**Port already in use**:
```bash
# Kill process using port 5173 (frontend)
npx kill-port 5173

# Kill process using port 8000 (backend)
npx kill-port 8000
```

**Virtual environment issues**:
```bash
# Recreate virtual environment
rm -rf backend/venv
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## Questions?

If you have questions about contributing:

- Check existing [Issues](https://github.com/H0NEYP0T-466/RAGbot/issues)
- Start a [Discussion](https://github.com/H0NEYP0T-466/RAGbot/discussions) (if enabled)
- Reach out to the maintainers

---

## Recognition

Contributors will be recognized in the project! We appreciate all contributions, big or small.

Thank you for contributing to RAGbot! 🎉
