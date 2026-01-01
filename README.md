# RAGbot

<p align="center">

  <!-- Core Badges -->
  <img src="https://img.shields.io/github/license/H0NEYP0T-466/RAGbot?style=for-the-badge&color=brightgreen" alt="GitHub License">
  <img src="https://img.shields.io/github/stars/H0NEYP0T-466/RAGbot?style=for-the-badge&color=yellow" alt="GitHub Stars">
  <img src="https://img.shields.io/github/forks/H0NEYP0T-466/RAGbot?style=for-the-badge&color=blue" alt="GitHub Forks">
  <img src="https://img.shields.io/github/issues/H0NEYP0T-466/RAGbot?style=for-the-badge&color=red" alt="GitHub Issues">
  <img src="https://img.shields.io/github/issues-pr/H0NEYP0T-466/RAGbot?style=for-the-badge&color=orange" alt="GitHub Pull Requests">
  <img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=for-the-badge" alt="Contributions Welcome">

  <!-- Activity Badges -->
  <img src="https://img.shields.io/github/last-commit/H0NEYP0T-466/RAGbot?style=for-the-badge&color=purple" alt="Last Commit">
  <img src="https://img.shields.io/github/commit-activity/m/H0NEYP0T-466/RAGbot?style=for-the-badge&color=teal" alt="Commit Activity">
  <img src="https://img.shields.io/github/repo-size/H0NEYP0T-466/RAGbot?style=for-the-badge&color=blueviolet" alt="Repo Size">
  <img src="https://img.shields.io/github/languages/code-size/H0NEYP0T-466/RAGbot?style=for-the-badge&color=indigo" alt="Code Size">

  <!-- Language Badges -->
  <img src="https://img.shields.io/github/languages/top/H0NEYP0T-466/RAGbot?style=for-the-badge&color=critical" alt="Top Language">
  <img src="https://img.shields.io/github/languages/count/H0NEYP0T-466/RAGbot?style=for-the-badge&color=success" alt="Languages Count">

  <!-- Community Badges -->
  <img src="https://img.shields.io/badge/Docs-Available-green?style=for-the-badge&logo=readthedocs&logoColor=white" alt="Documentation">
  <img src="https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red?style=for-the-badge" alt="Open Source Love">

</p>

<p align="center">
  <strong>Production-Ready RAG Chatbot with ChatGPT-like Interface</strong>
</p>

<p align="center">
  <em>Retrieval-Augmented Generation chatbot powered by LangChain, FAISS vector database, and LongCat LLM with a modern React frontend</em>
</p>

---

## 📖 Abstract

**RAGbot** is a production-ready **Retrieval-Augmented Generation (RAG) chatbot** that combines the power of large language models with domain-specific knowledge retrieval. Unlike traditional chatbots that rely solely on pre-trained knowledge, RAGbot:

- **Retrieves** relevant information from your custom document collection
- **Augments** LLM prompts with retrieved context
- **Generates** accurate, contextually-aware responses

### How It Works

1. **Document Indexing**: Your PDF/Markdown documents are embedded using HuggingFace Sentence Transformers (all-MiniLM-L6-v2)
2. **Vector Storage**: Embeddings stored in FAISS (Facebook AI Similarity Search) for fast retrieval
3. **Query Processing**: User questions are embedded and matched against the vector database
4. **Context Augmentation**: Top-k relevant documents are retrieved and added to the LLM prompt
5. **Response Generation**: LongCat LLM generates responses with retrieved context, improving accuracy

### Key Benefits

- 🎯 **Accurate Answers**: Responses grounded in your specific documents
- 🔄 **Up-to-Date**: Add new documents without retraining models
- 💬 **ChatGPT-like UX**: Familiar interface with markdown, code highlighting, LaTeX support
- 🚀 **Production-Ready**: FastAPI backend with comprehensive logging and error handling
- 🆓 **Cost-Effective**: Free LongCat LLM tier + open-source stack

---

## ✨ Key Highlights

- 🤖 **RAG Architecture** - Retrieval-Augmented Generation for accurate, context-aware responses
- 📚 **Document Knowledge Base** - PDF and Markdown document support with auto-indexing
- 🔍 **FAISS Vector Database** - Fast similarity search for relevant document retrieval
- 🧠 **LongCat LLM Integration** - Powered by advanced language model via OpenAI-compatible API
- 💬 **ChatGPT-like Interface** - Clean, modern chat UI with React 19 + TypeScript
- 📝 **Rich Markdown Rendering** - Syntax-highlighted code blocks, tables, lists
- 🧮 **LaTeX Math Support** - Render mathematical formulas with KaTeX
- ⚡ **Real-time Streaming** - Instant message delivery with loading indicators
- 🎨 **Dark Mode** - Eye-friendly dark theme
- 📊 **System Stats** - Monitor indexed documents and system health
- 🔧 **FastAPI Backend** - High-performance Python backend with OpenAPI docs
- 🌐 **LangChain Integration** - Industry-standard RAG pipeline framework

---

## 🏗️ Architecture

### System Overview

```
┌──────────────────────────────────────────────────────────────┐
│              Frontend (React + TypeScript)                   │
│  ┌───────────┐ ┌───────────┐ ┌──────────────────────┐       │
│  │  Chat UI  │ │  Markdown │ │   Message History    │       │
│  │ Component │ │  Renderer │ │   with Timestamps    │       │
│  └───────────┘ └───────────┘ └──────────────────────┘       │
│        │             │                    │                  │
│        └─────────────┴────────────────────┘                  │
│                      │                                       │
│             ┌────────▼────────┐                              │
│             │   API Client     │                              │
│             └────────┬────────┘                              │
└──────────────────────┼───────────────────────────────────────┘
                       │ HTTP/REST
┌──────────────────────▼───────────────────────────────────────┐
│              Backend (FastAPI + Python)                      │
│  ┌──────────────────────────────────────────────────────┐    │
│  │         API Routes (main.py)                         │    │
│  │  • POST /chat - Send message, get RAG response       │    │
│  │  • POST /reindex - Manually re-index documents       │    │
│  │  • GET /health - Health check                        │    │
│  │  • GET /stats - System statistics                    │    │
│  └────────────────────┬─────────────────────────────────┘    │
│                       │                                      │
│  ┌────────────────────▼─────────────────────────────────┐    │
│  │           RAG Pipeline (LangChain)                   │    │
│  │  ┌───────────────┐      ┌──────────────────────┐    │    │
│  │  │  Document     │      │   Query Embedding    │    │    │
│  │  │  Loader       │──────▶   (all-MiniLM-L6-v2) │    │    │
│  │  │ (PDF/MD)      │      └──────────┬───────────┘    │    │
│  │  └───────────────┘                 │                │    │
│  │                                    │                │    │
│  │  ┌───────────────┐      ┌──────────▼───────────┐    │    │
│  │  │  Embeddings   │      │   FAISS Vector DB    │    │    │
│  │  │  (HuggingFace)│◄─────│  Similarity Search   │    │    │
│  │  └───────────────┘      └──────────┬───────────┘    │    │
│  │                                    │                │    │
│  │                          ┌─────────▼──────────┐     │    │
│  │                          │  Top-K Retrieval   │     │    │
│  │                          │  (Relevant Docs)   │     │    │
│  │                          └─────────┬──────────┘     │    │
│  └────────────────────────────────────┼────────────────┘    │
│                                       │                     │
│  ┌────────────────────────────────────▼────────────────┐    │
│  │       LLM Client (LongCat via OpenAI API)           │    │
│  │  • Prompt: User Query + Retrieved Context          │    │
│  │  • Generate: Contextually-aware response           │    │
│  └────────────────────────────────────┬────────────────┘    │
│                                       │                     │
│  ┌────────────────────────────────────▼────────────────┐    │
│  │            Response with Citations                  │    │
│  │  • Answer based on retrieved documents             │    │
│  │  • Transparent context usage                       │    │
│  └─────────────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────────────┘
```

### RAG Pipeline Flow

1. **Document Ingestion**:
   - PDFs and Markdown files placed in `backend/data/`
   - Automatically indexed on server startup
   - Text chunked into manageable segments

2. **Embedding Generation**:
   - HuggingFace Sentence Transformers (`all-MiniLM-L6-v2`)
   - 384-dimensional dense vectors
   - CPU-optimized for fast inference

3. **Vector Storage**:
   - FAISS (Facebook AI Similarity Search)
   - In-memory index for fast retrieval
   - Cosine similarity matching

4. **Query Processing**:
   - User message embedded to same vector space
   - Top-K most similar document chunks retrieved
   - Typical K=3-5 for optimal context

5. **Prompt Augmentation**:
   - Retrieved documents prepended to user query
   - LLM receives: Context + Question
   - Grounded response generation

6. **Response Streaming**:
   - LongCat LLM via OpenAI-compatible API
   - Markdown-formatted response
   - Real-time delivery to frontend

---

## ✨ Features

### 🎨 Frontend Features

**Chat Interface:**
- Clean, ChatGPT-inspired design
- Dark mode for reduced eye strain
- Auto-scrolling message history
- Message timestamps
- Loading indicators during processing

**Markdown Rendering:**
- Full markdown support via `react-markdown`
- Syntax-highlighted code blocks (`react-syntax-highlighter`)
- Inline and block LaTeX math (KaTeX)
- Tables, lists, blockquotes
- Links and images

**User Experience:**
- Responsive design (mobile, tablet, desktop)
- Error handling with user-friendly messages
- Message retry on failure
- Clear visual feedback

### 🔧 Backend Features

**RAG Pipeline:**
- Automatic document indexing on startup
- PDF and Markdown document support
- Semantic search with FAISS vector database
- LangChain integration for robust RAG workflows
- Configurable retrieval parameters (top-k, chunk size)

**LLM Integration:**
- LongCat LLM via OpenAI-compatible API
- Free tier available for development
- Streaming response support
- Comprehensive error handling

**API & Logging:**
- FastAPI with automatic OpenAPI documentation
- Comprehensive server logging with timestamps
- Health check endpoint
- System statistics endpoint
- Manual re-indexing endpoint

**Embeddings:**
- HuggingFace Sentence Transformers
- `all-MiniLM-L6-v2` model (384-dim vectors)
- Fast CPU inference
- No GPU required

---

## Quick Start

### Prerequisites
- Node.js 18+
- Python 3.10+
- API Key:
  - `LONGCAT_API_KEY` - For LLM responses (free tier available)

### Frontend Setup

```bash
# Install dependencies
npm install

# Start development server
npm run dev
```

The frontend will be available at `http://localhost:5173`

### Backend Setup

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your API keys

# Add documents to data/ folder

# Start server
python -m app.main
```

The backend will be available at `http://localhost:8000`

## Project Structure

```
├── src/                    # Frontend source
│   ├── components/         # React components
│   ├── services/          # API services
│   └── types/             # TypeScript types
├── backend/               # Backend source
│   ├── app/               # FastAPI application
│   │   ├── rag/          # RAG pipeline
│   │   ├── llm/          # LLM client
│   │   └── utils/        # Utilities
│   ├── data/             # Document storage
│   └── faiss_index/      # FAISS vector index
└── public/               # Static assets
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/chat` | Send message and get AI response |
| POST | `/reindex` | Manually re-index documents |
| GET | `/health` | Health check |
| GET | `/stats` | System statistics |

## 🚀 Deployment

### Environment Variables

**Frontend (.env):**
```bash
VITE_API_URL=http://localhost:8000  # Development
# VITE_API_URL=https://your-backend.com  # Production
```

**Backend (.env):**
```bash
# Required
LONGCAT_API_KEY=your_longcat_api_key_here

# Optional Configuration
EMBEDDING_MODEL=all-MiniLM-L6-v2  # HuggingFace model
CHUNK_SIZE=500  # Document chunk size
CHUNK_OVERLAP=50  # Chunk overlap for context
TOP_K_RETRIEVAL=3  # Number of documents to retrieve
```

### Frontend Deployment (Vercel)

```bash
# Build
npm run build

# Deploy
vercel

# Configure in Vercel dashboard:
# VITE_API_URL = https://your-backend-api.com
```

### Backend Deployment (Railway/Render)

**Option 1: Railway**
```bash
railway login
railway init
railway up
```

**Option 2: Render**
- Connect GitHub repository
- Build command: `pip install -r requirements.txt`
- Start command: `cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT`
- Add environment variables

**Option 3: Docker**
```dockerfile
# backend/Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download embedding model during build
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```bash
docker build -t ragbot-backend ./backend
docker run -p 8000:8000 -e LONGCAT_API_KEY=your_key ragbot-backend
```

---

## 📖 Usage Examples

### Adding Documents

1. Place your documents in `backend/data/`:
   ```
   backend/data/
   ├── documentation.pdf
   ├── research_paper.pdf
   └── notes.md
   ```

2. Restart the server or call `/reindex`:
   ```bash
   curl -X POST http://localhost:8000/reindex
   ```

### Asking Questions

**Example 1: Technical Documentation**
```
User: How do I configure the embedding model?
Bot: Based on the documentation, you can configure the embedding model 
     by setting the EMBEDDING_MODEL environment variable. The default 
     model is all-MiniLM-L6-v2 from HuggingFace...
```

**Example 2: Research Paper Query**
```
User: What were the main findings of the study?
Bot: According to the research paper, the study found three main results:
     1. The proposed method improved accuracy by 15%
     2. Processing time decreased by 40%
     3. Model size reduced by 30% without performance loss...
```

### API Usage

**Send a Chat Message:**
```bash
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "What is RAG?"}'
```

**Response:**
```json
{
  "response": "RAG (Retrieval-Augmented Generation) is a technique that...",
  "sources": [
    "documentation.pdf (chunk 1)",
    "notes.md (chunk 3)"
  ],
  "timestamp": "2025-01-01T12:00:00Z"
}
```

**Get System Stats:**
```bash
curl http://localhost:8000/stats
```

**Response:**
```json
{
  "indexed_documents": 5,
  "total_chunks": 127,
  "embedding_model": "all-MiniLM-L6-v2",
  "vector_dimension": 384
}
```

---

## Technologies

### Frontend
- React 19 with TypeScript
- Vite build tool
- react-markdown with remark-math
- react-syntax-highlighter
- KaTeX for LaTeX rendering

### Backend
- FastAPI
- LangChain
- FAISS vector database (CPU version)
- HuggingFace Sentence Transformers (all-MiniLM-L6-v2)
- LongCat LLM (via OpenAI-compatible API)

---

## 📄 Documentation

- [Contributing Guidelines](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security Policy](SECURITY.md)
- [License](LICENSE)

---

## 🤝 Contributing

We welcome contributions from the community! Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting a pull request.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **LangChain** - RAG pipeline framework
- **FAISS** - Fast vector similarity search
- **HuggingFace** - Sentence Transformers embeddings
- **LongCat** - LLM inference API
- **React** - Modern UI framework

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/H0NEYP0T-466">H0NEYP0T-466</a>
</p>

<p align="center">
  <a href="https://github.com/H0NEYP0T-466/RAGbot/issues">Report Bug</a>
  ·
  <a href="https://github.com/H0NEYP0T-466/RAGbot/issues">Request Feature</a>
</p>
