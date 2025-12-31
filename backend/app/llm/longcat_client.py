"""LongCat API client wrapper using OpenAI-compatible interface."""

from typing import Optional

from openai import OpenAI

from app.config import get_settings
from app.utils.logger import logger


class LongCatClient:
    """Client for interacting with LongCat API using OpenAI-compatible interface."""
    
    def __init__(self):
        self.settings = get_settings()
        self._client: Optional[OpenAI] = None
    
    def _get_client(self) -> OpenAI:
        """Get or create the OpenAI client configured for LongCat."""
        if self._client is None:
            self._client = OpenAI(
                api_key=self.settings.longcat_api_key,
                base_url="https://api.longcat.chat/openai"
            )
        return self._client
    
    def generate_response(
        self,
        system_prompt: str,
        context: str,
        user_question: str
    ) -> dict:
        """
        Generate a response from the LongCat LLM.
        
        Args:
            system_prompt: System instructions for the AI
            context: Retrieved document context
            user_question: User's question
        
        Returns:
            Dictionary containing response content and usage statistics
        """
        client = self._get_client()
        
        # Build the user message with context
        user_message = f"""Context:
{context}

User Question: {user_question}"""
        
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
        
        try:
            response = client.chat.completions.create(
                model=self.settings.llm_model,
                messages=messages,
                max_tokens=self.settings.llm_max_tokens,
                temperature=self.settings.llm_temperature
            )
            
            return {
                "content": response.choices[0].message.content,
                "usage": {
                    "prompt_tokens": response.usage.prompt_tokens if response.usage else 0,
                    "completion_tokens": response.usage.completion_tokens if response.usage else 0,
                    "total_tokens": response.usage.total_tokens if response.usage else 0
                }
            }
            
        except Exception as e:
            logger.error(f"LongCat API error: {str(e)}")
            raise RuntimeError(f"Failed to generate response: {str(e)}")


# Singleton instance
_client_instance: Optional[LongCatClient] = None


def get_longcat_client() -> LongCatClient:
    """Get the singleton LongCatClient instance."""
    global _client_instance
    if _client_instance is None:
        _client_instance = LongCatClient()
    return _client_instance
