"""Rich logging utilities for comprehensive server logging."""

import logging
import sys
from datetime import datetime
from typing import Optional


class RichLogger:
    """Custom logger for rich, formatted console output."""
    
    def __init__(self, name: str = "RAGbot"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        
        # Clear existing handlers
        self.logger.handlers.clear()
        
        # Create console handler with formatting
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.INFO)
        
        # Simple format - we'll add rich formatting manually
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        
        self.logger.addHandler(handler)
    
    def _get_timestamp(self) -> str:
        """Get formatted timestamp."""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def _separator(self, char: str = "=", length: int = 60) -> str:
        """Create separator line."""
        return char * length
    
    def log_query_start(self, user_input: str) -> None:
        """Log the start of a new query."""
        self.logger.info("")
        self.logger.info(self._separator("="))
        self.logger.info(f"[{self._get_timestamp()}] NEW QUERY RECEIVED")
        self.logger.info(self._separator("="))
        self.logger.info(f'USER INPUT: "{user_input}"')
        self.logger.info("")
    
    def log_retrieval_process(
        self, 
        k: int, 
        chunks_retrieved: int,
        results: list[dict]
    ) -> None:
        """Log the RAG retrieval process."""
        self.logger.info(self._separator("-"))
        self.logger.info("RAG RETRIEVAL PROCESS")
        self.logger.info(self._separator("-"))
        self.logger.info(f"Similarity Search: k={k}")
        self.logger.info(f"Retrieved Chunks: {chunks_retrieved}")
        self.logger.info("")
        self.logger.info("Similarity Scores:")
        
        for i, result in enumerate(results, 1):
            source = result.get('source', 'unknown')
            page = result.get('page', None)
            score = result.get('score', 0.0)
            
            page_info = f" (page {page})" if page is not None else ""
            self.logger.info(f"  {i}. Score: {score:.4f} | Source: {source}{page_info}")
        
        self.logger.info("")
        self.logger.info("Chunk Previews:")
        
        for i, result in enumerate(results, 1):
            content = result.get('content', '')[:100]
            self.logger.info(f'  [{i}] "{content}..."')
        
        self.logger.info("")
    
    def log_prompt(self, system_prompt: str, context: str, user_question: str) -> None:
        """Log the final prompt sent to LLM."""
        self.logger.info(self._separator("-"))
        self.logger.info("FINAL PROMPT SENT TO LLM")
        self.logger.info(self._separator("-"))
        self.logger.info(f"System: {system_prompt}")
        self.logger.info("")
        self.logger.info("Context:")
        
        # Log context with document markers
        context_parts = context.split("\n\n")
        for i, part in enumerate(context_parts[:5], 1):  # Limit to first 5
            preview = part[:150]
            self.logger.info(f"[Document {i}] {preview}...")
        
        self.logger.info("")
        self.logger.info(f"User Question: {user_question}")
        self.logger.info("")
    
    def log_response(
        self, 
        response: str, 
        prompt_tokens: int,
        completion_tokens: int,
        total_tokens: int,
        model: str,
        temperature: float,
        max_tokens: int,
        response_time: float
    ) -> None:
        """Log the LLM response."""
        self.logger.info(self._separator("-"))
        self.logger.info("LLM RESPONSE")
        self.logger.info(self._separator("-"))
        self.logger.info(f'Response: "{response[:200]}..."' if len(response) > 200 else f'Response: "{response}"')
        self.logger.info("")
        self.logger.info("Token Usage:")
        self.logger.info(f"  - Prompt Tokens: {prompt_tokens}")
        self.logger.info(f"  - Completion Tokens: {completion_tokens}")
        self.logger.info(f"  - Total Tokens: {total_tokens}")
        self.logger.info("")
        self.logger.info(f"Model: {model}")
        self.logger.info(f"Temperature: {temperature}")
        self.logger.info(f"Max Tokens: {max_tokens}")
        self.logger.info("")
        self.logger.info(f"Response Time: {response_time:.2f}s")
        self.logger.info(self._separator("="))
        self.logger.info("")
    
    def log_indexing_start(self, folder: str) -> None:
        """Log document indexing start."""
        self.logger.info("")
        self.logger.info(self._separator("="))
        self.logger.info(f"[{self._get_timestamp()}] DOCUMENT INDEXING")
        self.logger.info(self._separator("="))
        self.logger.info(f"Scanning folder: {folder}")
    
    def log_document_found(self, filename: str, doc_type: str) -> None:
        """Log found document."""
        self.logger.info(f"  Found: {filename} ({doc_type})")
    
    def log_indexing_complete(self, documents: int, chunks: int) -> None:
        """Log indexing completion."""
        self.logger.info("")
        self.logger.info(f"Indexed {documents} documents into {chunks} chunks")
        self.logger.info(self._separator("="))
        self.logger.info("")
    
    def log_error(self, error: str, context: Optional[str] = None) -> None:
        """Log error with optional context."""
        self.logger.error("")
        self.logger.error(self._separator("!"))
        self.logger.error(f"[{self._get_timestamp()}] ERROR")
        if context:
            self.logger.error(f"Context: {context}")
        self.logger.error(f"Error: {error}")
        self.logger.error(self._separator("!"))
        self.logger.error("")
    
    def info(self, message: str) -> None:
        """Log info message."""
        self.logger.info(f"[{self._get_timestamp()}] {message}")
    
    def warning(self, message: str) -> None:
        """Log warning message."""
        self.logger.warning(f"[{self._get_timestamp()}] WARNING: {message}")
    
    def error(self, message: str) -> None:
        """Log error message."""
        self.logger.error(f"[{self._get_timestamp()}] ERROR: {message}")


# Global logger instance
logger = RichLogger()
