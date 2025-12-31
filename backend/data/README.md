# Data Folder

Place your PDF and Markdown (.md) files in this folder for RAG indexing.

## Supported File Types:
- `.pdf` - PDF documents
- `.md` - Markdown files

## How It Works:
1. Drop your documents into this folder
2. The application will automatically index them on startup
3. Call `POST /reindex` to re-index documents without restarting

## Document Tips:
- Use descriptive filenames - they appear in source citations
- Ensure PDFs are text-based (not scanned images)
- Large documents will be automatically chunked for optimal retrieval
