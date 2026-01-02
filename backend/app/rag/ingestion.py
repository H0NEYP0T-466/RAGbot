"""Document loading, chunking, and embedding ingestion."""

import os
from datetime import datetime
from pathlib import Path
from typing import Optional

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    UnstructuredWordDocumentLoader,
)
from langchain_community.vectorstores import FAISS

from app.config import get_settings
from app.rag.vectorstore import get_vectorstore_manager
from app.utils.logger import logger


class DocumentIngestion:
    """Handles document loading, chunking, and vector store ingestion."""
    
    def __init__(self):
        self.settings = get_settings()
        self.vectorstore_manager = get_vectorstore_manager()
        self._last_indexed: Optional[datetime] = None
        self._documents_count: int = 0
        
        # Text splitter with configured chunk settings
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.settings.chunk_size,
            chunk_overlap=self.settings.chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )
    
    def _load_pdf(self, file_path: str) -> list:
        """Load a PDF document."""
        try:
            loader = PyPDFLoader(file_path)
            documents = loader.load()
            
            # Add source metadata
            for doc in documents:
                doc.metadata["source"] = os.path.basename(file_path)
                doc.metadata["file_type"] = "pdf"
            
            return documents
        except Exception as e:
            logger.error(f"Failed to load PDF {file_path}: {str(e)}")
            return []
    
    def _load_markdown(self, file_path: str) -> list:
        """Load a Markdown document."""
        try:
            loader = TextLoader(file_path, encoding="utf-8")
            documents = loader.load()
            
            # Add source metadata
            for doc in documents:
                doc.metadata["source"] = os.path.basename(file_path)
                doc.metadata["file_type"] = "markdown"
            
            return documents
        except Exception as e:
            logger.error(f"Failed to load Markdown {file_path}: {str(e)}")
            return []
    
    def _load_docx(self, file_path: str) -> list:
        """Load a Word document (.docx)."""
        try:
            loader = UnstructuredWordDocumentLoader(file_path)
            documents = loader.load()
            
            # Add source metadata
            for doc in documents:
                doc.metadata["source"] = os.path.basename(file_path)
                doc.metadata["file_type"] = "docx"
            
            return documents
        except Exception as e:
            logger.error(f"Failed to load DOCX {file_path}: {str(e)}")
            return []
    
    def _load_text(self, file_path: str) -> list:
        """Load a text document."""
        try:
            loader = TextLoader(file_path, encoding="utf-8")
            documents = loader.load()
            
            # Add source metadata
            for doc in documents:
                doc.metadata["source"] = os.path.basename(file_path)
                doc.metadata["file_type"] = "text"
            
            return documents
        except Exception as e:
            logger.error(f"Failed to load text {file_path}: {str(e)}")
            return []
    
    def scan_data_folder(self) -> list[dict]:
        """Scan the data folder for documents."""
        data_path = Path(self.settings.data_folder)
        
        if not data_path.exists():
            logger.warning(f"Data folder does not exist: {data_path}")
            os.makedirs(data_path, exist_ok=True)
            return []
        
        found_files = []
        
        for file_path in data_path.iterdir():
            if file_path.is_file():
                suffix = file_path.suffix.lower()
                if suffix == ".pdf":
                    found_files.append({
                        "path": str(file_path),
                        "name": file_path.name,
                        "type": "pdf"
                    })
                elif suffix == ".md":
                    found_files.append({
                        "path": str(file_path),
                        "name": file_path.name,
                        "type": "markdown"
                    })
                elif suffix == ".txt":
                    found_files.append({
                        "path": str(file_path),
                        "name": file_path.name,
                        "type": "text"
                    })
                elif suffix in [".docx", ".doc"]:
                    found_files.append({
                        "path": str(file_path),
                        "name": file_path.name,
                        "type": "docx"
                    })
        
        return found_files
    
    def load_or_create_index(self) -> tuple[int, int]:
        """
        Load existing FAISS index or create a new one if it doesn't exist.
        
        Returns:
            Tuple of (documents_count, chunks_count)
        """
        # Check if FAISS index already exists
        index_path = Path(self.settings.faiss_index_path)
        index_file = index_path / "index.faiss"
        
        if index_file.exists():
            # Try to load existing index
            logger.info(f"Found existing FAISS index at {self.settings.faiss_index_path}")
            try:
                vectorstore = self.vectorstore_manager.get_vectorstore()
                
                if vectorstore is not None:
                    # Get stats from the loaded index
                    stats = self.vectorstore_manager.get_collection_stats()
                    chunks_count = stats.get("total_chunks", 0)
                    
                    # Count documents in data folder
                    files = self.scan_data_folder()
                    self._documents_count = len(files)
                    
                    logger.info(f"Loaded existing index: {self._documents_count} documents, {chunks_count} chunks")
                    return self._documents_count, chunks_count
                else:
                    logger.warning("Index file exists but failed to load. Will create new index.")
            except Exception as e:
                logger.warning(f"Failed to load existing index: {str(e)}. Will create new index.")
        
        # No existing index or loading failed, create new index
        logger.info("No existing index found, creating new index from documents...")
        return self.index_documents()
    
    def index_documents(self) -> tuple[int, int]:
        """
        Index all documents from the data folder.
        
        Returns:
            Tuple of (documents_count, chunks_count)
        """
        logger.log_indexing_start(self.settings.data_folder)
        
        # Find all documents
        files = self.scan_data_folder()
        
        if not files:
            logger.warning("No documents found in data folder")
            return 0, 0
        
        # Load all documents
        all_documents = []
        
        for file_info in files:
            logger.log_document_found(file_info["name"], file_info["type"])
            
            if file_info["type"] == "pdf":
                docs = self._load_pdf(file_info["path"])
            elif file_info["type"] == "markdown":
                docs = self._load_markdown(file_info["path"])
            elif file_info["type"] == "text":
                docs = self._load_text(file_info["path"])
            elif file_info["type"] == "docx":
                docs = self._load_docx(file_info["path"])
            else:
                continue
            
            all_documents.extend(docs)
        
        if not all_documents:
            logger.warning("No documents could be loaded")
            return 0, 0
        
        # Split documents into chunks
        chunks = self.text_splitter.split_documents(all_documents)
        
        logger.info(f"Split {len(all_documents)} documents into {len(chunks)} chunks")
        
        # Reset the vector store and create new FAISS index
        self.vectorstore_manager.reset_vectorstore()
        
        # Create FAISS vectorstore from documents
        embeddings = self.vectorstore_manager.get_embeddings()
        vectorstore = FAISS.from_documents(chunks, embeddings)
        
        # Save the index to disk
        os.makedirs(self.settings.faiss_index_path, exist_ok=True)
        vectorstore.save_local(self.settings.faiss_index_path)
        
        # Update the cached vectorstore
        self.vectorstore_manager.set_vectorstore(vectorstore)
        
        # Update tracking
        self._documents_count = len(files)
        self._last_indexed = datetime.now()
        
        logger.log_indexing_complete(len(files), len(chunks))
        
        return len(files), len(chunks)
    
    def index_single_file(self, file_path: str) -> tuple[int, int]:
        """
        Incrementally index a single file by adding it to existing index.
        
        Args:
            file_path: Path to the file to index
        
        Returns:
            Tuple of (documents_count, chunks_count)
        """
        logger.info(f"Incrementally indexing file: {file_path}")
        
        # Get existing vectorstore
        vectorstore = self.vectorstore_manager.get_vectorstore()
        
        if vectorstore is None:
            # No existing index, do a full index instead
            # NOTE: This fallback ensures the system recovers gracefully if the
            # index doesn't exist. It only happens on first run or after index deletion.
            # For normal operation with an existing index, incremental updates are used.
            logger.warning("No existing index found, performing full index")
            return self.index_documents()
        
        # Load the single file
        file_name = os.path.basename(file_path)
        suffix = Path(file_path).suffix.lower()
        
        docs = []
        if suffix == ".pdf":
            docs = self._load_pdf(file_path)
        elif suffix == ".md":
            docs = self._load_markdown(file_path)
        elif suffix == ".txt":
            docs = self._load_text(file_path)
        elif suffix in [".docx", ".doc"]:
            docs = self._load_docx(file_path)
        
        if not docs:
            logger.warning(f"No content loaded from {file_path}")
            return self._documents_count, self.vectorstore_manager.get_collection_stats().get("total_chunks", 0)
        
        # Split into chunks
        chunks = self.text_splitter.split_documents(docs)
        
        if not chunks:
            logger.warning(f"No chunks created from {file_path}")
            return self._documents_count, self.vectorstore_manager.get_collection_stats().get("total_chunks", 0)
        
        logger.info(f"Adding {len(chunks)} chunks from {file_name} to existing index")
        
        # Add new chunks to existing vectorstore
        vectorstore.add_documents(chunks)
        
        # Save the updated index
        vectorstore.save_local(self.settings.faiss_index_path)
        
        # Update the cached vectorstore
        self.vectorstore_manager.set_vectorstore(vectorstore)
        
        # Get updated stats
        stats = self.vectorstore_manager.get_collection_stats()
        total_chunks = stats.get("total_chunks", 0)
        
        logger.info(f"Incremental indexing complete: added {len(chunks)} chunks, total now {total_chunks}")
        
        return self._documents_count, total_chunks
    
    def get_stats(self) -> dict:
        """Get indexing statistics."""
        collection_stats = self.vectorstore_manager.get_collection_stats()
        
        # Calculate approximate DB size
        index_path = Path(self.settings.faiss_index_path)
        total_size = 0
        if index_path.exists():
            for file in index_path.rglob("*"):
                if file.is_file():
                    total_size += file.stat().st_size
        
        size_str = f"{total_size / (1024 * 1024):.2f} MB"
        
        return {
            "total_documents": self._documents_count,
            "total_chunks": collection_stats.get("total_chunks", 0),
            "vector_db_size": size_str,
            "last_indexed": self._last_indexed.isoformat() if self._last_indexed else "Never"
        }


# Singleton instance
_ingestion_instance: Optional[DocumentIngestion] = None


def get_document_ingestion() -> DocumentIngestion:
    """Get the singleton DocumentIngestion instance."""
    global _ingestion_instance
    if _ingestion_instance is None:
        _ingestion_instance = DocumentIngestion()
    return _ingestion_instance
