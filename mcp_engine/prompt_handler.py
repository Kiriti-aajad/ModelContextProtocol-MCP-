# mcp_engine/prompt_handler.py

def build_prompt(user_query: str, schema_hint: str = "") -> str:
    """
    Builds a structured prompt for the LLM to generate SQL.
    """
    prompt = f"""
You are a helpful assistant that converts natural language questions into SQL queries.

User question:
"{user_query}"

Database schema:
{schema_hint}

Instructions:
- Generate a syntactically correct SQL query.
- Only use tables and columns from the schema.
- Return only the SQL code, nothing else.

Respond with only the SQL query:
"""
    return prompt.strip()
