"""FAISS vector store initialization and management."""

import os
import pickle
from typing import Optional

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from app.config import get_settings
from app.utils.logger import logger


class VectorStoreManager:
    """Manages the FAISS vector store for document embeddings."""
    
    _instance: Optional["VectorStoreManager"] = None
    
    def __init__(self):
        self.settings = get_settings()
        self._embeddings: Optional[HuggingFaceEmbeddings] = None
        self._vectorstore: Optional[FAISS] = None
    
    @classmethod
    def get_instance(cls) -> "VectorStoreManager":
        """Get singleton instance of VectorStoreManager."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def _get_embeddings(self) -> HuggingFaceEmbeddings:
        """Get or create HuggingFace embeddings instance."""
        if self._embeddings is None:
            # Using all-MiniLM-L6-v2 - a lightweight, fast, and free model
            # 384 dimensions, good quality for semantic search
            self._embeddings = HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L6-v2",
                model_kwargs={'device': 'cpu'},
                encode_kwargs={'normalize_embeddings': True}
            )
        return self._embeddings
    
    def get_vectorstore(self) -> FAISS:
        """Get or create the FAISS vector store."""
        if self._vectorstore is None:
            embeddings = self._get_embeddings()
            index_path = self.settings.faiss_index_path
            
            # Try to load existing index
            if os.path.exists(index_path) and os.path.exists(os.path.join(index_path, "index.faiss")):
                try:
                    self._vectorstore = FAISS.load_local(
                        index_path,
                        embeddings,
                        allow_dangerous_deserialization=True
                    )
                    logger.info(f"Loaded existing FAISS index from {index_path}")
                except Exception as e:
                    logger.warning(f"Failed to load existing index: {e}. Creating new index.")
                    self._vectorstore = None
            
            # If no existing index or loading failed, create empty vectorstore
            # We'll populate it during indexing
        
        return self._vectorstore
    
    def reset_vectorstore(self) -> None:
        """Reset the vector store by clearing the index."""
        try:
            # Reset the cached vectorstore
            self._vectorstore = None
            
            # Remove existing index files if they exist
            index_path = self.settings.faiss_index_path
            if os.path.exists(index_path):
                import shutil
                shutil.rmtree(index_path)
            
            logger.info(f"Vector store index has been reset")
            
        except Exception as e:
            logger.error(f"Failed to reset vector store: {str(e)}")
            raise
    
    def get_collection_stats(self) -> dict:
        """Get statistics about the current index."""
        try:
            vectorstore = self.get_vectorstore()
            
            if vectorstore is None:
                count = 0
            else:
                # FAISS stores documents in index.docstore._dict
                count = len(vectorstore.docstore._dict) if hasattr(vectorstore, 'docstore') else 0
            
            return {
                "total_chunks": count,
                "faiss_index_path": self.settings.faiss_index_path
            }
        except Exception as e:
            logger.error(f"Failed to get collection stats: {str(e)}")
            return {
                "total_chunks": 0,
                "faiss_index_path": self.settings.faiss_index_path,
                "error": str(e)
            }
    
    def is_connected(self) -> bool:
        """Check if the vector store is operational."""
        try:
            # For FAISS, we just check if embeddings can be created
            self._get_embeddings()
            return True
        except Exception:
            return False


# Convenience function to get the vector store manager
def get_vectorstore_manager() -> VectorStoreManager:
    """Get the singleton VectorStoreManager instance."""
    return VectorStoreManager.get_instance()
