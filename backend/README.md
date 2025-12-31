# RAG Chatbot Backend

A production-ready Python FastAPI backend for a RAG (Retrieval-Augmented Generation) chatbot.

## Features

- **Document Ingestion**: Automatically loads and indexes PDF and Markdown files
- **Vector Database**: Uses Chroma for embedded, persistent vector storage
- **RAG Pipeline**: Retrieves relevant document chunks and generates context-aware responses
- **LongCat LLM**: Uses LongCat-Flash-Chat model via OpenAI-compatible API
- **Comprehensive Logging**: Detailed console logs for all operations

## Requirements

- Python 3.10+
- API Keys:
  - `LONGCAT_API_KEY` - For LLM responses
  - `OPENAI_API_KEY` - For text embeddings

## Installation

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   ```bash
   cp .env.example .env
   # Edit .env and add your API keys
   ```

5. Add documents to index:
   - Place PDF and Markdown files in `data/` folder

6. Run the server:
   ```bash
   python -m app.main
   ```

The server will start at `http://localhost:8000`

## API Endpoints

### POST /chat
Send a message and get an AI-generated response.

**Request:**
```json
{
  "message": "What is machine learning?"
}
```

**Response:**
```json
{
  "response": "Machine learning is...",
  "sources": [
    {"source": "ml_guide.pdf", "page": 5, "score": 0.87}
  ],
  "tokens": {
    "prompt": 456,
    "completion": 89,
    "total": 545
  }
}
```

### POST /reindex
Manually trigger re-indexing of all documents.

**Response:**
```json
{
  "status": "success",
  "message": "Indexed 15 documents with 234 chunks"
}
```

### GET /health
Check the health status of the application.

**Response:**
```json
{
  "status": "healthy",
  "vector_db": "connected",
  "documents_indexed": 15,
  "total_chunks": 234
}
```

### GET /stats
Get detailed statistics about the RAG system.

**Response:**
```json
{
  "total_documents": 15,
  "total_chunks": 234,
  "vector_db_size": "45.2 MB",
  "last_indexed": "2025-12-31T10:30:00Z"
}
```

## Configuration

See `.env.example` for all configuration options:

| Variable | Description | Default |
|----------|-------------|---------|
| `LONGCAT_API_KEY` | LongCat API key | Required |
| `OPENAI_API_KEY` | OpenAI API key (for embeddings) | Required |
| `CHUNK_SIZE` | Document chunk size | 1000 |
| `CHUNK_OVERLAP` | Overlap between chunks | 200 |
| `SIMILARITY_K` | Number of chunks to retrieve | 5 |
| `LLM_MODEL` | LLM model name | LongCat-Flash-Chat |
| `LLM_TEMPERATURE` | LLM temperature | 0.7 |
| `LLM_MAX_TOKENS` | Max response tokens | 2000 |

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI app entry point
│   ├── config.py         # Configuration settings
│   ├── models.py         # Pydantic models
│   ├── rag/
│   │   ├── vectorstore.py  # Chroma DB management
│   │   ├── ingestion.py    # Document processing
│   │   └── retrieval.py    # RAG query logic
│   ├── llm/
│   │   └── longcat_client.py  # LLM client
│   └── utils/
│       └── logger.py      # Logging utilities
├── data/                  # Place documents here
├── chroma_db/            # Vector database storage
├── requirements.txt
├── .env.example
└── details.txt           # Setup instructions
```

## Troubleshooting

### No documents indexed
- Ensure documents are in the `data/` folder
- Check that files have `.pdf` or `.md` extensions
- Call `POST /reindex` to manually trigger indexing

### API key errors
- Verify API keys are set in `.env` file
- Check that keys are valid and have necessary permissions

### Vector database issues
- Delete the `chroma_db/` folder to reset
- Restart the server to re-initialize

## License

MIT License
