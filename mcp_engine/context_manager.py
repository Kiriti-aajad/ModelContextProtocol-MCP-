# mcp_engine/context_manager.py

from data.schema import get_schema_hint 

class SessionContext:
    def __init__(self):
        self.history = []

    def build_prompt(self, user_query: str) -> str:
        """
        Builds a prompt using schema info and user input.
        Tracks the interaction in history.
        """
        schema_hint = get_schema_hint()
        prompt = f"""
You are a data analyst assistant.

User query:
"{user_query}"

Database Schema:
{schema_hint}

Generate a valid SQL query using only the available tables and columns.
Return only the SQL query.
"""
        self.history.append({
            "user_query": user_query,
            "schema_used": schema_hint
        })
        return prompt.strip()

    def get_history(self):
        return self.history
