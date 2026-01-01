"""Conversation history management for RAG context window."""

import os
from datetime import datetime
from pathlib import Path
from typing import Optional

from app.config import get_settings
from app.utils.logger import logger


class ConversationHistory:
    """Manages conversation history logging to history.txt for RAG retrieval."""
    
    def __init__(self):
        self.settings = get_settings()
        self.history_file = Path(self.settings.data_folder) / "history.txt"
        self._ensure_history_file()
    
    def _ensure_history_file(self):
        """Ensure the history file exists."""
        # Create data folder if it doesn't exist
        os.makedirs(self.settings.data_folder, exist_ok=True)
        
        # Create history file if it doesn't exist
        if not self.history_file.exists():
            self.history_file.touch()
            logger.info(f"Created conversation history file at {self.history_file}")
    
    def append_conversation(self, user_prompt: str, llm_response: str):
        """
        Append a conversation turn to the history file.
        
        Args:
            user_prompt: The user's message/question
            llm_response: The LLM's response
        """
        try:
            timestamp = datetime.now().isoformat()
            
            # Format the conversation entry
            entry = f"""[Conversation - {timestamp}]
User: {user_prompt}
Assistant: {llm_response}

"""
            
            # Append to the history file
            with open(self.history_file, "a", encoding="utf-8") as f:
                f.write(entry)
            
            logger.info(f"Appended conversation to history: {len(user_prompt)} chars (user) + {len(llm_response)} chars (assistant)")
            
        except Exception as e:
            logger.error(f"Failed to append conversation to history: {str(e)}")


# Singleton instance
_history_instance: Optional[ConversationHistory] = None


def get_conversation_history() -> ConversationHistory:
    """Get the singleton ConversationHistory instance."""
    global _history_instance
    if _history_instance is None:
        _history_instance = ConversationHistory()
    return _history_instance
