"""RAG query logic and document retrieval."""

import asyncio
import time
from typing import Optional

from app.config import get_settings
from app.llm.longcat_client import get_longcat_client
from app.models import ChatResponse, Source, TokenUsage
from app.rag.history import get_conversation_history
from app.rag.ingestion import get_document_ingestion
from app.rag.vectorstore import get_vectorstore_manager
from app.utils.logger import logger


class RAGRetrieval:
    """Handles RAG query processing and document retrieval."""
    
    def __init__(self):
        self.settings = get_settings()
        self.vectorstore_manager = get_vectorstore_manager()
        self.llm_client = get_longcat_client()
    
    async def _reindex_history_async(self, history_file_path: str):
        """
        Background task to re-index the history file incrementally.
        
        Args:
            history_file_path: Path to the history.txt file
        """
        try:
            # Run the blocking indexing operation in a thread pool
            loop = asyncio.get_event_loop()
            await loop.run_in_executor(
                None,
                self._reindex_history_sync,
                history_file_path
            )
        except Exception as e:
            logger.warning(f"Background re-indexing failed: {str(e)}")
    
    def _reindex_history_sync(self, history_file_path: str):
        """
        Synchronous re-indexing of history file (runs in thread pool).
        
        Args:
            history_file_path: Path to the history.txt file
        """
        try:
            ingestion = get_document_ingestion()
            ingestion.index_single_file(history_file_path)
            logger.info("Re-indexed conversation history incrementally")
        except Exception as e:
            logger.warning(f"Failed to re-index history file: {str(e)}")
    
    def retrieve_relevant_chunks(self, query: str, k: Optional[int] = None) -> list[dict]:
        """
        Retrieve the most relevant document chunks for a query.
        
        Args:
            query: User query string
            k: Number of chunks to retrieve (defaults to settings.similarity_k)
        
        Returns:
            List of dictionaries containing chunk content and metadata
        """
        k = k or self.settings.similarity_k
        
        vectorstore = self.vectorstore_manager.get_vectorstore()
        
        if vectorstore is None:
            logger.warning("Vector store is not initialized. No documents indexed.")
            return []
        
        # Perform similarity search with scores
        results = vectorstore.similarity_search_with_score(query, k=k)
        
        chunks = []
        for doc, score in results:
            # FAISS returns L2 distance - lower is better
            # Convert to a similarity score (inverse of distance, normalized)
            # For L2 distance, we use 1/(1+distance+epsilon) for numerical stability
            similarity = 1 / (1 + score + 1e-8)
            
            chunk_info = {
                "content": doc.page_content,
                "source": doc.metadata.get("source", "unknown"),
                "page": doc.metadata.get("page", None),
                "score": similarity
            }
            chunks.append(chunk_info)
        
        return chunks
    
    def build_context(self, chunks: list[dict]) -> str:
        """Build context string from retrieved chunks."""
        context_parts = []
        for i, chunk in enumerate(chunks, 1):
            source = chunk.get("source", "unknown")
            page = chunk.get("page", None)
            page_info = f" (page {page})" if page is not None else ""
            
            context_parts.append(
                f"[Document {i} - {source}{page_info}]\n{chunk['content']}"
            )
        
        return "\n\n".join(context_parts)
    
    def query(self, user_input: str) -> ChatResponse:
        """
        Process a user query through the RAG pipeline.
        
        Args:
            user_input: User's question or query
        
        Returns:
            ChatResponse containing the answer and metadata
        """
        start_time = time.time()
        
        # Log query start
        logger.log_query_start(user_input)
        
        # Step 1: Retrieve relevant chunks
        chunks = self.retrieve_relevant_chunks(user_input)
        
        # Log retrieval process
        logger.log_retrieval_process(
            k=self.settings.similarity_k,
            chunks_retrieved=len(chunks),
            results=chunks
        )
        
        # Step 2: Build context
        context = self.build_context(chunks)
        
        # Step 3: Build prompt
        system_prompt = self.settings.system_prompt
        
        # Log the prompt
        logger.log_prompt(system_prompt, context, user_input)
        
        # Step 4: Get LLM response
        llm_response = self.llm_client.generate_response(
            system_prompt=system_prompt,
            context=context,
            user_question=user_input
        )
        
        response_time = time.time() - start_time
        
        # Log the response
        logger.log_response(
            response=llm_response["content"],
            prompt_tokens=llm_response["usage"]["prompt_tokens"],
            completion_tokens=llm_response["usage"]["completion_tokens"],
            total_tokens=llm_response["usage"]["total_tokens"],
            model=self.settings.llm_model,
            temperature=self.settings.llm_temperature,
            max_tokens=self.settings.llm_max_tokens,
            response_time=response_time
        )
        
        # Step 5: Append conversation to history file
        conversation_history = get_conversation_history()
        conversation_history.append_conversation(user_input, llm_response["content"])
        
        # Build response
        sources = [
            Source(
                source=chunk["source"],
                page=chunk.get("page"),
                score=chunk["score"]
            )
            for chunk in chunks
        ]
        
        tokens = TokenUsage(
            prompt=llm_response["usage"]["prompt_tokens"],
            completion=llm_response["usage"]["completion_tokens"],
            total=llm_response["usage"]["total_tokens"]
        )
        
        response_obj = ChatResponse(
            response=llm_response["content"],
            sources=sources,
            tokens=tokens
        )
        
        # Step 6: Trigger background re-indexing of history file only
        # NOTE: Re-indexing is now done asynchronously after returning the response
        # to avoid blocking the API response. Only the history.txt file is re-indexed
        # incrementally for better performance.
        try:
            history_file_path = conversation_history.history_file
            # Create background task for re-indexing
            asyncio.create_task(self._reindex_history_async(str(history_file_path)))
        except Exception as e:
            logger.warning(f"Failed to schedule background re-indexing: {str(e)}")
        
        return response_obj


# Singleton instance
_retrieval_instance: Optional[RAGRetrieval] = None


def get_rag_retrieval() -> RAGRetrieval:
    """Get the singleton RAGRetrieval instance."""
    global _retrieval_instance
    if _retrieval_instance is None:
        _retrieval_instance = RAGRetrieval()
    return _retrieval_instance
