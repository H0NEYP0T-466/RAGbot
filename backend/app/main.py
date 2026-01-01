"""FastAPI application entry point with startup events and routes."""

import traceback
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.config import get_settings
from app.models import (
    ChatRequest,
    ChatResponse,
    ErrorResponse,
    HealthResponse,
    ReindexResponse,
    StatsResponse,
)
from app.rag.ingestion import get_document_ingestion
from app.rag.retrieval import get_rag_retrieval
from app.rag.vectorstore import get_vectorstore_manager
from app.utils.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events - startup and shutdown."""
    # Startup
    logger.info("Starting RAG Chatbot Backend...")
    
    settings = get_settings()
    logger.info(f"Data folder: {settings.data_folder}")
    logger.info(f"FAISS Index path: {settings.faiss_index_path}")
    logger.info(f"LLM Model: {settings.llm_model}")
    
    # Auto-index documents on startup
    try:
        ingestion = get_document_ingestion()
        docs, chunks = ingestion.index_documents()
        logger.info(f"Startup indexing complete: {docs} documents, {chunks} chunks")
    except Exception as e:
        logger.error(f"Startup indexing failed: {str(e)}")
        logger.warning("Server starting without indexed documents. Call /reindex to index manually.")
    
    logger.info("RAG Chatbot Backend started successfully!")
    
    yield
    
    # Shutdown
    logger.info("Shutting down RAG Chatbot Backend...")


# Create FastAPI app
app = FastAPI(
    title="RAG Chatbot API",
    description="A production-ready RAG (Retrieval-Augmented Generation) chatbot API",
    version="1.0.0",
    lifespan=lifespan
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/chat", response_model=ChatResponse, responses={400: {"model": ErrorResponse}, 500: {"model": ErrorResponse}})
async def chat(request: ChatRequest) -> ChatResponse:
    """
    Process a chat message through the RAG pipeline.
    
    - Retrieves relevant document chunks
    - Builds context from retrieved chunks
    - Generates response using LongCat LLM
    """
    try:
        if not request.message.strip():
            raise HTTPException(status_code=400, detail="Message cannot be empty")
        
        retrieval = get_rag_retrieval()
        response = retrieval.query(request.message)
        return response
        
    except HTTPException:
        raise
    except Exception as e:
        logger.log_error(str(e), "Chat endpoint")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Failed to process message: {str(e)}")


@app.post("/reindex", response_model=ReindexResponse, responses={500: {"model": ErrorResponse}})
async def reindex() -> ReindexResponse:
    """
    Manually trigger re-indexing of all documents in the data folder.
    
    This will:
    - Scan the data folder for PDF and Markdown files
    - Load and chunk all documents
    - Generate embeddings and store in vector database
    """
    try:
        ingestion = get_document_ingestion()
        docs, chunks = ingestion.index_documents()
        
        return ReindexResponse(
            status="success",
            message=f"Indexed {docs} documents with {chunks} chunks"
        )
        
    except Exception as e:
        logger.log_error(str(e), "Reindex endpoint")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Failed to reindex: {str(e)}")


@app.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    """
    Check the health status of the application.
    
    Returns vector database connection status and indexed document counts.
    """
    try:
        vectorstore_manager = get_vectorstore_manager()
        is_connected = vectorstore_manager.is_connected()
        stats = vectorstore_manager.get_collection_stats()
        
        ingestion = get_document_ingestion()
        ingestion_stats = ingestion.get_stats()
        
        return HealthResponse(
            status="healthy" if is_connected else "unhealthy",
            vector_db="connected" if is_connected else "disconnected",
            documents_indexed=ingestion_stats.get("total_documents", 0),
            total_chunks=stats.get("total_chunks", 0)
        )
        
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        return HealthResponse(
            status="unhealthy",
            vector_db="error",
            documents_indexed=0,
            total_chunks=0
        )


@app.get("/stats", response_model=StatsResponse)
async def stats() -> StatsResponse:
    """
    Get detailed statistics about the RAG system.
    
    Returns document counts, chunk counts, database size, and last indexing time.
    """
    try:
        ingestion = get_document_ingestion()
        stats = ingestion.get_stats()
        
        return StatsResponse(
            total_documents=stats.get("total_documents", 0),
            total_chunks=stats.get("total_chunks", 0),
            vector_db_size=stats.get("vector_db_size", "0 MB"),
            last_indexed=stats.get("last_indexed", "Never")
        )
        
    except Exception as e:
        logger.error(f"Stats endpoint failed: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to get stats: {str(e)}")


if __name__ == "__main__":
    settings = get_settings()
    uvicorn.run(
        "app.main:app",
        host=settings.backend_host,
        port=settings.backend_port,
        reload=True
    )
