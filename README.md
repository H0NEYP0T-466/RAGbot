# RAGbot

<p align="center">

  <!-- Core -->
  ![GitHub License](https://img.shields.io/github/license/H0NEYP0T-466/RAGbot?style=for-the-badge&color=brightgreen)
  ![GitHub Stars](https://img.shields.io/github/stars/H0NEYP0T-466/RAGbot?style=for-the-badge&color=yellow)
  ![GitHub Forks](https://img.shields.io/github/forks/H0NEYP0T-466/RAGbot?style=for-the-badge&color=blue)
  ![GitHub Issues](https://img.shields.io/github/issues/H0NEYP0T-466/RAGbot?style=for-the-badge&color=red)
  ![GitHub Pull Requests](https://img.shields.io/github/issues-pr/H0NEYP0T-466/RAGbot?style=for-the-badge&color=orange)
  ![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=for-the-badge)

  <!-- Activity -->
  ![Last Commit](https://img.shields.io/github/last-commit/H0NEYP0T-466/RAGbot?style=for-the-badge&color=purple)
  ![Commit Activity](https://img.shields.io/github/commit-activity/m/H0NEYP0T-466/RAGbot?style=for-the-badge&color=teal)
  ![Repo Size](https://img.shields.io/github/repo-size/H0NEYP0T-466/RAGbot?style=for-the-badge&color=blueviolet)
  ![Code Size](https://img.shields.io/github/languages/code-size/H0NEYP0T-466/RAGbot?style=for-the-badge&color=indigo)

  <!-- Languages -->
  ![Top Language](https://img.shields.io/github/languages/top/H0NEYP0T-466/RAGbot?style=for-the-badge&color=critical)
  ![Languages Count](https://img.shields.io/github/languages/count/H0NEYP0T-466/RAGbot?style=for-the-badge&color=success)

  <!-- Community -->
  ![Documentation](https://img.shields.io/badge/Docs-Available-green?style=for-the-badge&logo=readthedocs&logoColor=white)
  ![Open Source Love](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red?style=for-the-badge)

</p>

<p align="center">
  A production-ready <strong>RAG (Retrieval-Augmented Generation) chatbot</strong> with a ChatGPT-like frontend and Python FastAPI backend.
</p>

---

## 🔗 Links

- 🌐 **Demo**: [*TRY-HERE*](https://ra-gbot.vercel.app/)
- 📖 **Documentation**: Available in this README
- 🐛 **Issues**: [Report a bug](https://github.com/H0NEYP0T-466/RAGbot/issues)
- 💡 **Contributing**: [Contribution Guide](CONTRIBUTING.md)

---

## 📑 Table of Contents

- [✨ Features](#-features)
- [🚀 Installation](#-installation)
  - [Prerequisites](#prerequisites)
  - [Frontend Setup](#frontend-setup)
  - [Backend Setup](#backend-setup)
- [⚡ Usage](#-usage)
- [📂 Project Structure](#-project-structure)
- [🛠 Tech Stack](#-tech-stack)
- [📦 Dependencies & Packages](#-dependencies--packages)
- [🔌 API Endpoints](#-api-endpoints)
- [⚙️ Configuration](#️-configuration)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [🛡 Security](#-security)
- [📏 Code of Conduct](#-code-of-conduct)

---

## ✨ Features

### Frontend
- 💬 Clean, ChatGPT-inspired chat interface
- 📝 Full Markdown rendering with syntax-highlighted code blocks
- ➗ LaTeX/Math formula support
- 📜 Auto-scrolling chat history with timestamps
- ⏳ Loading indicators and error handling
- 🎨 Responsive design with dark mode support

### Backend
- 🚀 FastAPI with automatic document indexing
- 🔍 RAG pipeline with FAISS vector database
- 🤖 Free Sentence Transformers embeddings (all-MiniLM-L6-v2)
- 🦙 LongCat LLM integration via OpenAI-compatible API
- 📊 Comprehensive server logging
- 📄 PDF and Markdown document support

---

## 🚀 Installation

### Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js** 18+ ([Download](https://nodejs.org/))
- **Python** 3.10+ ([Download](https://www.python.org/))
- **npm** (comes with Node.js) or **yarn**
- **API Key**: `LONGCAT_API_KEY` - For LLM responses (free tier available)

### Frontend Setup

```bash
# Clone the repository
git clone https://github.com/H0NEYP0T-466/RAGbot.git
cd RAGbot

# Install dependencies
npm install

# Start development server
npm run dev
```

The frontend will be available at **`http://localhost:5173`**

### Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env and add your API keys

# Add documents to data/ folder (PDFs, Markdown files)

# Start the server
python -m app.main
```

The backend will be available at **`http://localhost:8000`**

---

## ⚡ Usage

1. **Start the backend server** (follow Backend Setup above)
2. **Start the frontend** (follow Frontend Setup above)
3. **Open your browser** and navigate to `http://localhost:5173`
4. **Start chatting!** Type your questions and the RAG bot will respond using your indexed documents

### Example Queries

```
"What is the main topic of the documents?"
"Summarize the key points from the documentation"
"Explain [specific concept] from the indexed content"
```

---

## 📂 Project Structure

```
RAGbot/
├── src/                    # Frontend source code
│   ├── components/         # React components
│   │   ├── Chat.tsx        # Main chat interface
│   │   ├── Message.tsx     # Message component
│   │   └── ...
│   ├── services/           # API service layer
│   │   └── api.ts          # API client
│   ├── types/              # TypeScript type definitions
│   └── App.tsx             # Root component
├── backend/                # Backend source code
│   ├── app/                # FastAPI application
│   │   ├── rag/            # RAG pipeline implementation
│   │   ├── llm/            # LLM client integration
│   │   ├── utils/          # Utility functions
│   │   ├── main.py         # FastAPI entry point
│   │   ├── models.py       # Pydantic models
│   │   └── config.py       # Configuration management
│   ├── data/               # Document storage directory
│   ├── faiss_index/        # FAISS vector index storage
│   └── requirements.txt    # Python dependencies
├── public/                 # Static assets
├── .github/                # GitHub templates and workflows
├── package.json            # Node.js dependencies
├── vite.config.ts          # Vite configuration
├── tsconfig.json           # TypeScript configuration
└── README.md               # This file
```

---

## 🛠 Tech Stack

### Languages

![TypeScript](https://img.shields.io/badge/TypeScript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white)
![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![JavaScript](https://img.shields.io/badge/JavaScript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

### Frameworks & Libraries

![React](https://img.shields.io/badge/React-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Vite](https://img.shields.io/badge/Vite-%23646CFF.svg?style=for-the-badge&logo=vite&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)

### AI & Machine Learning

![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=000)

### Databases & Vector Stores

![FAISS](https://img.shields.io/badge/FAISS-Vector%20DB-blue?style=for-the-badge)

### DevOps / Tools

![ESLint](https://img.shields.io/badge/ESLint-4B3263?style=for-the-badge&logo=eslint&logoColor=white)
![Git](https://img.shields.io/badge/Git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![NPM](https://img.shields.io/badge/NPM-%23CB3837.svg?style=for-the-badge&logo=npm&logoColor=white)

---

## 📦 Dependencies & Packages

<details>
<summary><strong>Runtime Dependencies (Frontend)</strong></summary>

[![katex](https://img.shields.io/npm/v/katex?style=for-the-badge&label=katex&logo=npm)](https://www.npmjs.com/package/katex) - LaTeX math rendering library

[![react](https://img.shields.io/npm/v/react?style=for-the-badge&label=react&logo=react)](https://www.npmjs.com/package/react) - JavaScript library for building user interfaces

[![react-dom](https://img.shields.io/npm/v/react-dom?style=for-the-badge&label=react-dom&logo=react)](https://www.npmjs.com/package/react-dom) - React package for working with the DOM

[![react-markdown](https://img.shields.io/npm/v/react-markdown?style=for-the-badge&label=react-markdown&logo=markdown)](https://www.npmjs.com/package/react-markdown) - Markdown component for React

[![react-syntax-highlighter](https://img.shields.io/npm/v/react-syntax-highlighter?style=for-the-badge&label=react-syntax-highlighter&logo=npm)](https://www.npmjs.com/package/react-syntax-highlighter) - Syntax highlighting for React

[![rehype-katex](https://img.shields.io/npm/v/rehype-katex?style=for-the-badge&label=rehype-katex&logo=npm)](https://www.npmjs.com/package/rehype-katex) - Rehype plugin to render math with KaTeX

[![remark-gfm](https://img.shields.io/npm/v/remark-gfm?style=for-the-badge&label=remark-gfm&logo=markdown)](https://www.npmjs.com/package/remark-gfm) - Remark plugin for GitHub Flavored Markdown

[![remark-math](https://img.shields.io/npm/v/remark-math?style=for-the-badge&label=remark-math&logo=npm)](https://www.npmjs.com/package/remark-math) - Remark plugin for math

[![uuid](https://img.shields.io/npm/v/uuid?style=for-the-badge&label=uuid&logo=npm)](https://www.npmjs.com/package/uuid) - Generate RFC-compliant UUIDs

</details>

<details>
<summary><strong>Dev Dependencies (Frontend)</strong></summary>

[![@eslint/js](https://img.shields.io/npm/v/@eslint/js?style=for-the-badge&label=@eslint/js&logo=eslint)](https://www.npmjs.com/package/@eslint/js) - ESLint JavaScript configuration

[![@types/node](https://img.shields.io/npm/v/@types/node?style=for-the-badge&label=@types/node&logo=node.js)](https://www.npmjs.com/package/@types/node) - TypeScript definitions for Node.js

[![@types/react](https://img.shields.io/npm/v/@types/react?style=for-the-badge&label=@types/react&logo=react)](https://www.npmjs.com/package/@types/react) - TypeScript definitions for React

[![@types/react-dom](https://img.shields.io/npm/v/@types/react-dom?style=for-the-badge&label=@types/react-dom&logo=react)](https://www.npmjs.com/package/@types/react-dom) - TypeScript definitions for React DOM

[![@types/react-syntax-highlighter](https://img.shields.io/npm/v/@types/react-syntax-highlighter?style=for-the-badge&label=@types/react-syntax-highlighter&logo=npm)](https://www.npmjs.com/package/@types/react-syntax-highlighter) - TypeScript definitions for react-syntax-highlighter

[![@types/uuid](https://img.shields.io/npm/v/@types/uuid?style=for-the-badge&label=@types/uuid&logo=npm)](https://www.npmjs.com/package/@types/uuid) - TypeScript definitions for uuid

[![@vitejs/plugin-react](https://img.shields.io/npm/v/@vitejs/plugin-react?style=for-the-badge&label=@vitejs/plugin-react&logo=vite)](https://www.npmjs.com/package/@vitejs/plugin-react) - Official Vite plugin for React

[![eslint](https://img.shields.io/npm/v/eslint?style=for-the-badge&label=eslint&logo=eslint)](https://www.npmjs.com/package/eslint) - Linting utility for JavaScript and TypeScript

[![eslint-plugin-react-hooks](https://img.shields.io/npm/v/eslint-plugin-react-hooks?style=for-the-badge&label=eslint-plugin-react-hooks&logo=react)](https://www.npmjs.com/package/eslint-plugin-react-hooks) - ESLint rules for React Hooks

[![eslint-plugin-react-refresh](https://img.shields.io/npm/v/eslint-plugin-react-refresh?style=for-the-badge&label=eslint-plugin-react-refresh&logo=react)](https://www.npmjs.com/package/eslint-plugin-react-refresh) - ESLint plugin for React Refresh

[![globals](https://img.shields.io/npm/v/globals?style=for-the-badge&label=globals&logo=npm)](https://www.npmjs.com/package/globals) - Global identifiers from different JavaScript environments

[![typescript](https://img.shields.io/npm/v/typescript?style=for-the-badge&label=typescript&logo=typescript)](https://www.npmjs.com/package/typescript) - TypeScript language

[![typescript-eslint](https://img.shields.io/npm/v/typescript-eslint?style=for-the-badge&label=typescript-eslint&logo=typescript)](https://www.npmjs.com/package/typescript-eslint) - Monorepo for all tooling for TypeScript with ESLint

[![vite](https://img.shields.io/npm/v/vite?style=for-the-badge&label=vite&logo=vite)](https://www.npmjs.com/package/vite) - Next generation frontend tooling

</details>

<details>
<summary><strong>Runtime Dependencies (Backend - Python)</strong></summary>

[![fastapi](https://img.shields.io/pypi/v/fastapi?style=for-the-badge&label=fastapi&logo=fastapi)](https://pypi.org/project/fastapi/) - Modern web framework for building APIs with Python

[![uvicorn](https://img.shields.io/pypi/v/uvicorn?style=for-the-badge&label=uvicorn&logo=python)](https://pypi.org/project/uvicorn/) - ASGI web server implementation for Python

[![python-dotenv](https://img.shields.io/pypi/v/python-dotenv?style=for-the-badge&label=python-dotenv&logo=python)](https://pypi.org/project/python-dotenv/) - Read key-value pairs from .env file

[![langchain](https://img.shields.io/pypi/v/langchain?style=for-the-badge&label=langchain&logo=python)](https://pypi.org/project/langchain/) - Building applications with LLMs through composability

[![langchain-community](https://img.shields.io/pypi/v/langchain-community?style=for-the-badge&label=langchain-community&logo=python)](https://pypi.org/project/langchain-community/) - Community contributed LangChain integrations

[![faiss-cpu](https://img.shields.io/pypi/v/faiss-cpu?style=for-the-badge&label=faiss-cpu&logo=python)](https://pypi.org/project/faiss-cpu/) - Library for efficient similarity search and clustering

[![sentence-transformers](https://img.shields.io/pypi/v/sentence-transformers?style=for-the-badge&label=sentence-transformers&logo=python)](https://pypi.org/project/sentence-transformers/) - Compute dense vector representations for sentences

[![pypdf](https://img.shields.io/pypi/v/pypdf?style=for-the-badge&label=pypdf&logo=python)](https://pypi.org/project/pypdf/) - PDF library for Python

[![pydantic](https://img.shields.io/pypi/v/pydantic?style=for-the-badge&label=pydantic&logo=python)](https://pypi.org/project/pydantic/) - Data validation using Python type annotations

[![python-multipart](https://img.shields.io/pypi/v/python-multipart?style=for-the-badge&label=python-multipart&logo=python)](https://pypi.org/project/python-multipart/) - Streaming multipart parser for Python

[![pydantic-settings](https://img.shields.io/pypi/v/pydantic-settings?style=for-the-badge&label=pydantic-settings&logo=python)](https://pypi.org/project/pydantic-settings/) - Settings management using Pydantic

[![openai](https://img.shields.io/pypi/v/openai?style=for-the-badge&label=openai&logo=openai)](https://pypi.org/project/openai/) - OpenAI Python client library

</details>

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/chat` | Send a message and receive an AI-generated response |
| `POST` | `/reindex` | Manually trigger document re-indexing |
| `GET` | `/health` | Check backend health status |
| `GET` | `/stats` | Get system statistics and indexed document count |

### Example Request

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What is RAG?"}'
```

---

## ⚙️ Configuration

### Frontend

Set the `VITE_API_URL` environment variable to configure the backend API URL:

```bash
# .env
VITE_API_URL=http://localhost:8000
```

Default: `http://localhost:8000`

### Backend

Configure the backend using environment variables in `backend/.env`:

```bash
# API Keys
LONGCAT_API_KEY=your_api_key_here

# Server Configuration
HOST=0.0.0.0
PORT=8000

# RAG Configuration
EMBEDDING_MODEL=all-MiniLM-L6-v2
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
```

See `backend/.env.example` for all available configuration options.

---

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details on:

- How to submit pull requests
- Coding standards and style guide
- Testing requirements
- Reporting bugs and requesting features

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🛡 Security

If you discover a security vulnerability, please review our [Security Policy](SECURITY.md) for responsible disclosure guidelines.

---

## 📏 Code of Conduct

This project adheres to the Contributor Covenant [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

---

<p align="center">Made with ❤️ by <a href="https://github.com/H0NEYP0T-466">H0NEYP0T-466</a></p>
