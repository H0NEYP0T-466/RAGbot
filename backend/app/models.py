"""Pydantic models for request/response validation."""

from typing import Optional
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Request model for chat endpoint."""
    message: str = Field(..., min_length=1, description="User message to process")


class Source(BaseModel):
    """Document source information."""
    source: str = Field(..., description="Source document name")
    page: Optional[int] = Field(None, description="Page number if applicable")
    score: float = Field(..., description="Similarity score")


class TokenUsage(BaseModel):
    """Token usage information."""
    prompt: int = Field(..., description="Prompt tokens used")
    completion: int = Field(..., description="Completion tokens used")
    total: int = Field(..., description="Total tokens used")


class ChatResponse(BaseModel):
    """Response model for chat endpoint."""
    response: str = Field(..., description="AI assistant response")
    sources: list[Source] = Field(default_factory=list, description="Source documents")
    tokens: TokenUsage = Field(..., description="Token usage")


class ReindexResponse(BaseModel):
    """Response model for reindex endpoint."""
    status: str = Field(..., description="Operation status")
    message: str = Field(..., description="Status message")


class HealthResponse(BaseModel):
    """Response model for health endpoint."""
    status: str = Field(..., description="Health status")
    vector_db: str = Field(..., description="Vector database status")
    documents_indexed: int = Field(..., description="Number of documents indexed")
    total_chunks: int = Field(..., description="Total number of chunks")


class StatsResponse(BaseModel):
    """Response model for stats endpoint."""
    total_documents: int = Field(..., description="Total documents")
    total_chunks: int = Field(..., description="Total chunks")
    vector_db_size: str = Field(..., description="Vector database size")
    last_indexed: str = Field(..., description="Last indexed timestamp")


class ErrorResponse(BaseModel):
    """Error response model."""
    detail: str = Field(..., description="Error message")
