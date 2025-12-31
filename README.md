# RAG Chatbot

A production-ready **RAG (Retrieval-Augmented Generation) chatbot** with a ChatGPT-like frontend and Python FastAPI backend.

![RAG Chatbot](https://img.shields.io/badge/React-TypeScript-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-Python-green) ![Chroma](https://img.shields.io/badge/Chroma-Vector%20DB-purple)

## Features

### Frontend
- Clean, ChatGPT-inspired chat interface
- Full Markdown rendering with syntax-highlighted code blocks
- LaTeX/Math formula support
- Auto-scrolling chat history with timestamps
- Loading indicators and error handling
- Responsive design with dark mode support

### Backend
- FastAPI with automatic document indexing
- RAG pipeline with Chroma vector database
- LongCat LLM integration via OpenAI-compatible API
- Comprehensive server logging
- PDF and Markdown document support

## Quick Start

### Prerequisites
- Node.js 18+
- Python 3.10+
- API Keys:
  - `LONGCAT_API_KEY` - For LLM responses
  - `OPENAI_API_KEY` - For text embeddings

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
│   └── chroma_db/        # Vector database
└── public/               # Static assets
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/chat` | Send message and get AI response |
| POST | `/reindex` | Manually re-index documents |
| GET | `/health` | Health check |
| GET | `/stats` | System statistics |

## Configuration

### Frontend
Set `VITE_API_URL` environment variable to configure the backend URL (default: `http://localhost:8000`)

### Backend
See `backend/.env.example` for all configuration options.

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
- Chroma vector database
- OpenAI embeddings (text-embedding-3-small)
- LongCat LLM (via OpenAI-compatible API)

## License

MIT License
