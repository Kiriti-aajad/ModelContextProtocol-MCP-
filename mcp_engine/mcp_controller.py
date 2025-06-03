"""MCP Controller - orchestrates context, prompt creation, LLM interaction, and response formatting."""

import logging
from typing import Optional

from .context_manager import ContextManager
from .prompt_handler import PromptHandler
from .response_formatter import ResponseFormatter

logger = logging.getLogger(__name__)

class MCPController:
    def __init__(
        self,
        context_manager: Optional[ContextManager] = None,
        prompt_handler: Optional[PromptHandler] = None,
        response_formatter: Optional[ResponseFormatter] = None,
        llm_client=None  # Inject your LLM client here
    ):
        self.context_manager = context_manager or ContextManager()
        self.prompt_handler = prompt_handler or PromptHandler()
        self.response_formatter = response_formatter or ResponseFormatter()
        self.llm_client = llm_client

    def handle_query(self, user_id: str, user_query: str) -> str:
        """
        Process user query through MCP pipeline.

        Args:
            user_id: Unique user identifier.
            user_query: The user's input query string.

        Returns:
            Formatted response string from the LLM.
        """
        logger.info(f"Handling query for user {user_id}: {user_query}")

        # Load prior conversation context
        context = self.context_manager.load_context(user_id)

        # Create prompt from user query and context
        prompt = self.prompt_handler.create_prompt(user_query, context)
        logger.debug(f"Generated prompt for user {user_id}: {prompt}")

        # Query LLM client - replace with real call
        llm_response = self._query_llm(prompt)

        # Format the LLM response for user
        formatted_response = self.response_formatter.format_response(llm_response)

        # Update context with latest query and response
        self.context_manager.update_context(user_id, {
            "last_query": user_query,
            "last_response": formatted_response,
        })

        logger.info(f"Returning response to user {user_id}")
        return formatted_response

    def _query_llm(self, prompt: str) -> str:
        """
        Query the LLM client with the prompt.

        Override this method with actual LLM integration.

        Args:
            prompt: The prompt string to send to LLM.

        Returns:
            Raw response string from LLM.
        """
        if not self.llm_client:
            # Placeholder fallback
            logger.warning("LLM client not configured. Returning placeholder response.")
            return f"[Simulated LLM Response] Prompt was: {prompt}"

        # Example LLM client call:
        # response = self.llm_client.query(prompt)
        # return response

        # Temporary:
        return "[LLM response placeholder]"
