"""Chroma vector store initialization and management."""

import os
from typing import Optional

import chromadb
from chromadb.config import Settings as ChromaSettings
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

from app.config import get_settings
from app.utils.logger import logger


class VectorStoreManager:
    """Manages the Chroma vector store for document embeddings."""
    
    _instance: Optional["VectorStoreManager"] = None
    
    def __init__(self):
        self.settings = get_settings()
        self._embeddings: Optional[OpenAIEmbeddings] = None
        self._vectorstore: Optional[Chroma] = None
        self._client: Optional[chromadb.Client] = None
    
    @classmethod
    def get_instance(cls) -> "VectorStoreManager":
        """Get singleton instance of VectorStoreManager."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def _get_embeddings(self) -> OpenAIEmbeddings:
        """Get or create OpenAI embeddings instance."""
        if self._embeddings is None:
            self._embeddings = OpenAIEmbeddings(
                model="text-embedding-3-small",
                openai_api_key=self.settings.openai_api_key
            )
        return self._embeddings
    
    def _get_chroma_client(self) -> chromadb.PersistentClient:
        """Get or create Chroma client."""
        if self._client is None:
            # Ensure the directory exists
            os.makedirs(self.settings.vector_db_path, exist_ok=True)
            
            self._client = chromadb.PersistentClient(
                path=self.settings.vector_db_path,
                settings=ChromaSettings(
                    anonymized_telemetry=False,
                    allow_reset=True
                )
            )
        return self._client
    
    def get_vectorstore(self) -> Chroma:
        """Get or create the Chroma vector store."""
        if self._vectorstore is None:
            embeddings = self._get_embeddings()
            client = self._get_chroma_client()
            
            self._vectorstore = Chroma(
                client=client,
                collection_name=self.settings.collection_name,
                embedding_function=embeddings
            )
        return self._vectorstore
    
    def reset_vectorstore(self) -> None:
        """Reset the vector store by clearing the collection."""
        try:
            client = self._get_chroma_client()
            
            # Delete the collection if it exists
            try:
                client.delete_collection(self.settings.collection_name)
            except Exception:
                pass  # Collection might not exist
            
            # Reset the cached vectorstore
            self._vectorstore = None
            
            logger.info(f"Vector store collection '{self.settings.collection_name}' has been reset")
            
        except Exception as e:
            logger.error(f"Failed to reset vector store: {str(e)}")
            raise
    
    def get_collection_stats(self) -> dict:
        """Get statistics about the current collection."""
        try:
            vectorstore = self.get_vectorstore()
            collection = vectorstore._collection
            
            count = collection.count()
            
            return {
                "collection_name": self.settings.collection_name,
                "total_chunks": count,
                "vector_db_path": self.settings.vector_db_path
            }
        except Exception as e:
            logger.error(f"Failed to get collection stats: {str(e)}")
            return {
                "collection_name": self.settings.collection_name,
                "total_chunks": 0,
                "vector_db_path": self.settings.vector_db_path,
                "error": str(e)
            }
    
    def is_connected(self) -> bool:
        """Check if the vector store is connected and operational."""
        try:
            self.get_vectorstore()
            return True
        except Exception:
            return False


# Convenience function to get the vector store manager
def get_vectorstore_manager() -> VectorStoreManager:
    """Get the singleton VectorStoreManager instance."""
    return VectorStoreManager.get_instance()
