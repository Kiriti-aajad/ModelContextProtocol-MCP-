"""Generates LLM prompt from user input and session context."""

from typing import Dict, Optional

class PromptHandler:
    def __init__(self):
        pass

    def create_prompt(self, user_query: str, context: Optional[Dict] = None) -> str:
        """
        Combine user query with relevant context to generate an LLM prompt.

        Args:
            user_query: The user's current input query.
            context: Optional dictionary of previous context.

        Returns:
            A string prompt formatted for LLM consumption.
        """
        context_section = ""
        if context:
            # Pick what to include from context to avoid prompt bloat
            history = context.get("history", [])
            if history:
                context_section = "Conversation History:\n"
                for entry in history[-5:]:  # last 5 exchanges max
                    context_section += f"User: {entry.get('user')}\nAssistant: {entry.get('assistant')}\n"
                context_section += "\n"

        prompt = (
            f"{context_section}"
            f"User Query:\n{user_query}\n"
            "Provide a detailed and helpful response."
        )
        return prompt
