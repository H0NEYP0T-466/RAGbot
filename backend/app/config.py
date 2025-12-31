"""Configuration settings for the RAG chatbot application."""

import os
from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # LongCat API Configuration
    longcat_api_key: str = ""
    
    # OpenAI API Configuration (for embeddings)
    openai_api_key: str = ""
    
    # Vector Database Configuration
    vector_db_path: str = "./chroma_db"
    collection_name: str = "rag_documents"
    
    # Data Configuration
    data_folder: str = "./data"
    
    # RAG Configuration
    chunk_size: int = 1000
    chunk_overlap: int = 200
    similarity_k: int = 5
    
    # LLM Configuration
    llm_model: str = "LongCat-Flash-Chat"
    llm_temperature: float = 0.7
    llm_max_tokens: int = 2000
    
    # Server Configuration
    backend_host: str = "0.0.0.0"
    backend_port: int = 8000
    
    # System Prompt
    system_prompt: str = (
        "You are a helpful AI assistant. Answer questions based on the provided context documents. "
        "If the answer isn't in the context, say so clearly. Be concise and accurate."
    )
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
