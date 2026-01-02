# Contributing to RAGbot

First off, thank you for considering contributing to RAGbot! It's people like you that make RAGbot such a great tool. 🎉

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Pull Requests](#pull-requests)
- [Development Setup](#development-setup)
- [Style Guidelines](#style-guidelines)
  - [Git Commit Messages](#git-commit-messages)
  - [Code Style](#code-style)
- [Testing](#testing)
- [Documentation](#documentation)

---

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

---

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the [existing issues](https://github.com/H0NEYP0T-466/RAGbot/issues) to avoid duplicates. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples** to demonstrate the steps
- **Describe the behavior you observed** and explain what you expected instead
- **Include screenshots or animated GIFs** if applicable
- **Provide your environment details** (OS, Node.js version, Python version, etc.)

Use our [bug report template](.github/ISSUE_TEMPLATE/bug_report.yml) to file a bug report.

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide a detailed description** of the suggested enhancement
- **Explain why this enhancement would be useful** to most users
- **List any alternatives you've considered**

Use our [feature request template](.github/ISSUE_TEMPLATE/feature_request.yml) to suggest an enhancement.

### Pull Requests

Follow these steps to submit a pull request:

1. **Fork the repository** and create your branch from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following our [style guidelines](#style-guidelines)

3. **Test your changes thoroughly**:
   - Run the linter: `npm run lint`
   - Build the project: `npm run build`
   - Test both frontend and backend

4. **Commit your changes** with clear commit messages (see [Git Commit Messages](#git-commit-messages))

5. **Push to your fork** and submit a pull request to the `main` branch

6. **Fill out the pull request template** completely

7. **Wait for review** - maintainers will review your PR and may request changes

**Tips for a successful PR:**
- Keep changes focused and atomic
- Write clear, self-documenting code
- Add tests for new functionality
- Update documentation as needed
- Ensure all tests pass before submitting

---

## Development Setup

### Prerequisites

- Node.js 18+
- Python 3.10+
- Git

### Setting Up the Development Environment

1. **Clone your fork**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/RAGbot.git
   cd RAGbot
   ```

2. **Install frontend dependencies**:
   ```bash
   npm install
   ```

3. **Set up the backend**:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   ```bash
   cp backend/.env.example backend/.env
   # Edit backend/.env with your configuration
   ```

5. **Start development servers**:
   
   Terminal 1 (Backend):
   ```bash
   cd backend
   source venv/bin/activate
   python -m app.main
   ```
   
   Terminal 2 (Frontend):
   ```bash
   npm run dev
   ```

---

## Style Guidelines

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line
- Consider using conventional commit format:
  - `feat:` for new features
  - `fix:` for bug fixes
  - `docs:` for documentation changes
  - `style:` for formatting changes
  - `refactor:` for code refactoring
  - `test:` for adding tests
  - `chore:` for maintenance tasks

**Example:**
```
feat: add PDF upload functionality

- Implement file upload component
- Add backend endpoint for PDF processing
- Update documentation

Closes #123
```

### Code Style

#### Frontend (TypeScript/React)

- Use **TypeScript** for type safety
- Follow **ESLint** configuration (run `npm run lint`)
- Use **functional components** with hooks
- Use **meaningful variable and function names**
- Keep components **small and focused**
- Add **JSDoc comments** for complex functions

**Example:**
```typescript
/**
 * Sends a chat message to the backend API
 * @param message - The user's message
 * @returns Promise with the AI response
 */
export const sendChatMessage = async (message: string): Promise<ChatResponse> => {
  // Implementation
};
```

#### Backend (Python)

- Follow **PEP 8** style guide
- Use **type hints** for function parameters and return types
- Write **docstrings** for all public functions and classes
- Keep functions **focused and single-purpose**
- Use **meaningful variable names**

**Example:**
```python
def process_document(file_path: str) -> List[str]:
    """
    Process a document and split it into chunks.
    
    Args:
        file_path: Path to the document file
        
    Returns:
        List of text chunks
    """
    # Implementation
```

---

## Testing

### Frontend Testing

```bash
# Run linter
npm run lint

# Build the project
npm run build
```

### Backend Testing

```bash
cd backend
source venv/bin/activate

# Run the application and test endpoints
python -m app.main
```

### Manual Testing Checklist

- [ ] Frontend loads without errors
- [ ] Backend API responds correctly
- [ ] Chat functionality works end-to-end
- [ ] Document indexing completes successfully
- [ ] Error messages display properly
- [ ] UI is responsive on different screen sizes

---

## Documentation

- Update the README.md if you change functionality
- Add JSDoc/docstrings to new functions
- Update API documentation for new endpoints
- Include code examples for new features
- Keep documentation clear and concise

---

## Questions?

Feel free to:
- Open a [Discussion](https://github.com/H0NEYP0T-466/RAGbot/discussions) for questions
- Ask in an existing issue
- Reach out to the maintainers

---

Thank you for contributing to RAGbot! 🚀
