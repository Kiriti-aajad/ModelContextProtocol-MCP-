"""Formats raw LLM responses before returning to clients."""

class ResponseFormatter:
    def __init__(self):
        pass

    def format_response(self, llm_response: str) -> str:
        """
        Clean and format raw LLM response text.

        Args:
            llm_response: Raw response from the LLM.

        Returns:
            Formatted string suitable for client consumption.
        """
        if not llm_response:
            return "I'm sorry, I did not receive a response."

        # Example formatting: strip, remove excessive spaces, add safety checks
        response = llm_response.strip()
        # Additional formatting or sanitizing can go here

        return response
