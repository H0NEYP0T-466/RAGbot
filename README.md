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
  <strong>A production-ready RAG (Retrieval-Augmented Generation) chatbot with a ChatGPT-like frontend and Python FastAPI backend.</strong>
</p>

---

## 🔗 Quick Links

- [Demo](#-quick-start) | [Installation](#-installation) | [Usage](#-usage) | [Features](#-features)
- [Issues](https://github.com/H0NEYP0T-466/RAGbot/issues) | [Contributing](CONTRIBUTING.md)
- [Security](SECURITY.md) | [Code of Conduct](CODE_OF_CONDUCT.md)

---

## 📑 Table of Contents

- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Folder Structure](#-folder-structure)
- [API Endpoints](#-api-endpoints)
- [Tech Stack](#-tech-stack)
- [Dependencies & Packages](#-dependencies--packages)
- [Configuration](#-configuration)
- [Contributing](#-contributing)
- [License](#-license)
- [Security](#-security)
- [Code of Conduct](#-code-of-conduct)

---

## ✨ Features

### 🎨 Frontend
- ✅ Clean, ChatGPT-inspired chat interface
- ✅ Full Markdown rendering with syntax-highlighted code blocks
- ✅ LaTeX/Math formula support
- ✅ Auto-scrolling chat history with timestamps
- ✅ Loading indicators and error handling
- ✅ Responsive design with dark mode support

### ⚙️ Backend
- ✅ FastAPI with automatic document indexing
- ✅ RAG pipeline with FAISS vector database
- ✅ Free Sentence Transformers embeddings (all-MiniLM-L6-v2)
- ✅ LongCat LLM integration via OpenAI-compatible API
- ✅ Comprehensive server logging
- ✅ PDF and Markdown document support

---

## 🚀 Installation

### Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js** 18+ ([Download](https://nodejs.org/))
- **Python** 3.10+ ([Download](https://python.org/))
- **Git** ([Download](https://git-scm.com/))
- **API Key**: `LONGCAT_API_KEY` - For LLM responses (free tier available)

### Setup Steps

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/H0NEYP0T-466/RAGbot.git
cd RAGbot
```

#### 2️⃣ Frontend Setup

```bash
# Install dependencies
npm install

# Start development server
npm run dev
```

The frontend will be available at **http://localhost:5173**

#### 3️⃣ Backend Setup

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your API keys

# Add documents to data/ folder
# (Place your PDF or Markdown files here)

# Start server
python -m app.main
```

The backend will be available at **http://localhost:8000**

---

## ⚡ Usage

### Web Interface

1. **Start both frontend and backend servers** (see [Installation](#-installation))
2. **Open your browser** and navigate to `http://localhost:5173`
3. **Start chatting!** Type your questions in the chat input
4. The bot will search your documents and provide contextual answers

### API Usage

You can also interact with the backend directly:

```bash
# Send a chat message
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What is RAG?"}'

# Check system health
curl http://localhost:8000/health

# Get system statistics
curl http://localhost:8000/stats

# Manually reindex documents
curl -X POST http://localhost:8000/reindex
```

### Adding Documents

1. Place your PDF or Markdown files in `backend/data/`
2. The system will automatically index them on startup
3. Or manually trigger reindexing via the `/reindex` endpoint

---

## 📂 Folder Structure

```
RAGbot/
├── .github/                    # GitHub configuration
│   ├── ISSUE_TEMPLATE/        # Issue templates
│   └── pull_request_template.md
├── backend/                   # Backend source
│   ├── app/                   # FastAPI application
│   │   ├── llm/              # LLM client integration
│   │   ├── rag/              # RAG pipeline implementation
│   │   ├── utils/            # Utility functions
│   │   ├── config.py         # Configuration management
│   │   ├── main.py           # FastAPI entry point
│   │   └── models.py         # Pydantic models
│   ├── data/                 # Document storage
│   ├── faiss_index/          # FAISS vector index storage
│   ├── .env.example          # Environment variables template
│   └── requirements.txt      # Python dependencies
├── src/                       # Frontend source
│   ├── components/           # React components
│   │   ├── ChatBox.tsx       # Chat interface component
│   │   ├── ChatMessage.tsx   # Message display component
│   │   └── MarkdownRenderer.tsx
│   ├── services/             # API services
│   │   └── api.ts            # API client
│   ├── types/                # TypeScript type definitions
│   │   └── chat.ts           # Chat-related types
│   ├── App.tsx               # Main app component
│   └── main.tsx              # React entry point
├── public/                    # Static assets
├── .gitignore                # Git ignore rules
├── eslint.config.js          # ESLint configuration
├── index.html                # HTML template
├── package.json              # Node.js dependencies
├── package-lock.json         # Locked dependencies
├── tsconfig.json             # TypeScript configuration
├── vite.config.ts            # Vite build configuration
├── CONTRIBUTING.md           # Contributing guidelines
├── CODE_OF_CONDUCT.md        # Code of conduct
├── SECURITY.md               # Security policy
├── LICENSE                   # MIT License
└── README.md                 # This file
```

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/chat` | Send message and get AI response |
| `POST` | `/reindex` | Manually re-index documents |
| `GET` | `/health` | Health check endpoint |
| `GET` | `/stats` | System statistics and metrics |

---

## 🛠 Tech Stack

### Languages

![TypeScript](https://img.shields.io/badge/TypeScript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white)
![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![JavaScript](https://img.shields.io/badge/JavaScript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![HTML5](https://img.shields.io/badge/HTML5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)

### Frameworks & Libraries

![React](https://img.shields.io/badge/React-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![Vite](https://img.shields.io/badge/Vite-%23646CFF.svg?style=for-the-badge&logo=vite&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)

### AI/ML & Databases

![FAISS](https://img.shields.io/badge/FAISS-Vector%20DB-purple?style=for-the-badge)
![HuggingFace](https://img.shields.io/badge/HuggingFace-%23FFD21E.svg?style=for-the-badge&logo=huggingface&logoColor=black)
![Sentence Transformers](https://img.shields.io/badge/Sentence%20Transformers-NLP-blue?style=for-the-badge)

### DevOps / CI / Tools

![ESLint](https://img.shields.io/badge/ESLint-4B3263?style=for-the-badge&logo=eslint&logoColor=white)
![Git](https://img.shields.io/badge/Git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![npm](https://img.shields.io/badge/npm-%23CB3837.svg?style=for-the-badge&logo=npm&logoColor=white)
![pip](https://img.shields.io/badge/pip-3775A9?style=for-the-badge&logo=pypi&logoColor=white)

---

## 📦 Dependencies & Packages

<details open>
<summary><strong>📥 Runtime Dependencies (Frontend - Node.js)</strong></summary>

[![katex](https://img.shields.io/npm/v/katex?style=for-the-badge&label=katex)](https://www.npmjs.com/package/katex) - LaTeX math rendering  
[![react](https://img.shields.io/npm/v/react?style=for-the-badge&label=react)](https://www.npmjs.com/package/react) - React library  
[![react-dom](https://img.shields.io/npm/v/react-dom?style=for-the-badge&label=react-dom)](https://www.npmjs.com/package/react-dom) - React DOM bindings  
[![react-markdown](https://img.shields.io/npm/v/react-markdown?style=for-the-badge&label=react-markdown)](https://www.npmjs.com/package/react-markdown) - Markdown component for React  
[![react-syntax-highlighter](https://img.shields.io/npm/v/react-syntax-highlighter?style=for-the-badge&label=react-syntax-highlighter)](https://www.npmjs.com/package/react-syntax-highlighter) - Syntax highlighting component  
[![rehype-katex](https://img.shields.io/npm/v/rehype-katex?style=for-the-badge&label=rehype-katex)](https://www.npmjs.com/package/rehype-katex) - Rehype plugin for KaTeX  
[![remark-gfm](https://img.shields.io/npm/v/remark-gfm?style=for-the-badge&label=remark-gfm)](https://www.npmjs.com/package/remark-gfm) - GitHub Flavored Markdown support  
[![remark-math](https://img.shields.io/npm/v/remark-math?style=for-the-badge&label=remark-math)](https://www.npmjs.com/package/remark-math) - Math support for Markdown  
[![uuid](https://img.shields.io/npm/v/uuid?style=for-the-badge&label=uuid)](https://www.npmjs.com/package/uuid) - UUID generation  

</details>

<details>
<summary><strong>🛠 Dev/Build/Test Dependencies (Frontend - Node.js)</strong></summary>

[![@eslint/js](https://img.shields.io/npm/v/@eslint/js?style=for-the-badge&label=@eslint/js)](https://www.npmjs.com/package/@eslint/js) - ESLint JavaScript rules  
[![@types/node](https://img.shields.io/npm/v/@types/node?style=for-the-badge&label=@types/node)](https://www.npmjs.com/package/@types/node) - TypeScript definitions for Node.js  
[![@types/react](https://img.shields.io/npm/v/@types/react?style=for-the-badge&label=@types/react)](https://www.npmjs.com/package/@types/react) - TypeScript definitions for React  
[![@types/react-dom](https://img.shields.io/npm/v/@types/react-dom?style=for-the-badge&label=@types/react-dom)](https://www.npmjs.com/package/@types/react-dom) - TypeScript definitions for React DOM  
[![@types/react-syntax-highlighter](https://img.shields.io/npm/v/@types/react-syntax-highlighter?style=for-the-badge&label=@types/react-syntax-highlighter)](https://www.npmjs.com/package/@types/react-syntax-highlighter) - TypeScript definitions  
[![@types/uuid](https://img.shields.io/npm/v/@types/uuid?style=for-the-badge&label=@types/uuid)](https://www.npmjs.com/package/@types/uuid) - TypeScript definitions for UUID  
[![@vitejs/plugin-react](https://img.shields.io/npm/v/@vitejs/plugin-react?style=for-the-badge&label=@vitejs/plugin-react)](https://www.npmjs.com/package/@vitejs/plugin-react) - Vite React plugin  
[![eslint](https://img.shields.io/npm/v/eslint?style=for-the-badge&label=eslint)](https://www.npmjs.com/package/eslint) - JavaScript/TypeScript linter  
[![eslint-plugin-react-hooks](https://img.shields.io/npm/v/eslint-plugin-react-hooks?style=for-the-badge&label=eslint-plugin-react-hooks)](https://www.npmjs.com/package/eslint-plugin-react-hooks) - React Hooks linting  
[![eslint-plugin-react-refresh](https://img.shields.io/npm/v/eslint-plugin-react-refresh?style=for-the-badge&label=eslint-plugin-react-refresh)](https://www.npmjs.com/package/eslint-plugin-react-refresh) - React Refresh linting  
[![globals](https://img.shields.io/npm/v/globals?style=for-the-badge&label=globals)](https://www.npmjs.com/package/globals) - Global identifiers  
[![typescript](https://img.shields.io/npm/v/typescript?style=for-the-badge&label=typescript)](https://www.npmjs.com/package/typescript) - TypeScript compiler  
[![typescript-eslint](https://img.shields.io/npm/v/typescript-eslint?style=for-the-badge&label=typescript-eslint)](https://www.npmjs.com/package/typescript-eslint) - TypeScript ESLint tooling  
[![vite](https://img.shields.io/npm/v/vite?style=for-the-badge&label=vite)](https://www.npmjs.com/package/vite) - Next-generation frontend build tool  

</details>

<details open>
<summary><strong>📥 Runtime Dependencies (Backend - Python)</strong></summary>

[![fastapi](https://img.shields.io/pypi/v/fastapi?style=for-the-badge&label=fastapi)](https://pypi.org/project/fastapi/) - Modern web framework for APIs  
[![uvicorn](https://img.shields.io/pypi/v/uvicorn?style=for-the-badge&label=uvicorn)](https://pypi.org/project/uvicorn/) - ASGI server  
[![python-dotenv](https://img.shields.io/pypi/v/python-dotenv?style=for-the-badge&label=python-dotenv)](https://pypi.org/project/python-dotenv/) - Environment variable management  
[![langchain](https://img.shields.io/pypi/v/langchain?style=for-the-badge&label=langchain)](https://pypi.org/project/langchain/) - LLM application framework  
[![langchain-community](https://img.shields.io/pypi/v/langchain-community?style=for-the-badge&label=langchain-community)](https://pypi.org/project/langchain-community/) - LangChain community integrations  
[![faiss-cpu](https://img.shields.io/pypi/v/faiss-cpu?style=for-the-badge&label=faiss-cpu)](https://pypi.org/project/faiss-cpu/) - FAISS vector similarity search (CPU version)  
[![sentence-transformers](https://img.shields.io/pypi/v/sentence-transformers?style=for-the-badge&label=sentence-transformers)](https://pypi.org/project/sentence-transformers/) - Sentence embedding models  
[![pypdf](https://img.shields.io/pypi/v/pypdf?style=for-the-badge&label=pypdf)](https://pypi.org/project/pypdf/) - PDF parsing library  
[![pydantic](https://img.shields.io/pypi/v/pydantic?style=for-the-badge&label=pydantic)](https://pypi.org/project/pydantic/) - Data validation using Python type hints  
[![python-multipart](https://img.shields.io/pypi/v/python-multipart?style=for-the-badge&label=python-multipart)](https://pypi.org/project/python-multipart/) - Multipart form data parser  
[![pydantic-settings](https://img.shields.io/pypi/v/pydantic-settings?style=for-the-badge&label=pydantic-settings)](https://pypi.org/project/pydantic-settings/) - Settings management for Pydantic  
[![openai](https://img.shields.io/pypi/v/openai?style=for-the-badge&label=openai)](https://pypi.org/project/openai/) - OpenAI API client  

</details>

---

## ⚙️ Configuration

### Frontend Configuration

Set the following environment variable to configure the backend URL:

- `VITE_API_URL` - Backend API URL (default: `http://localhost:8000`)

Create a `.env` file in the root directory:

```env
VITE_API_URL=http://localhost:8000
```

### Backend Configuration

See `backend/.env.example` for all available configuration options:

```env
LONGCAT_API_KEY=your_api_key_here
LONGCAT_BASE_URL=https://api.longcat.com/v1
MODEL_NAME=longcat-7b
EMBEDDING_MODEL=all-MiniLM-L6-v2
DOCUMENTS_PATH=./data
INDEX_PATH=./faiss_index
```

---

## 🤝 Contributing

We welcome contributions from the community! Please read our [Contributing Guidelines](CONTRIBUTING.md) to get started.

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🛡 Security

We take security seriously. If you discover a security vulnerability, please follow our [Security Policy](SECURITY.md) to report it responsibly.

---

## 📏 Code of Conduct

This project adheres to the [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

---

<p align="center">Made with ❤️ by H0NEYP0T-466</p>
