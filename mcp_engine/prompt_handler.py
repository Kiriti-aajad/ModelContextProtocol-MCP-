class PromptHandler:
    def __init__(self, context_manager):
        self.context_manager = context_manager

    def build_prompt(self, user_query):
        # Collect relevant schema context (optional logic can be added here)
        all_tables = self.context_manager.list_all_tables()

        schema_context = []
        for table in all_tables:
            columns = self.context_manager.get_columns_in_table(table)
            col_descriptions = ", ".join([col["column_name"] for col in columns])
            schema_context.append(f"{table}: {col_descriptions}")

        schema_snippet = "\n".join(schema_context[:10])  # Limit context to avoid overload

        # Construct the prompt
        prompt = f"""
You are a database query assistant.

Schema Overview (partial):
{schema_snippet}

User Query:
{user_query}

Based on the above schema, understand the user’s intent and help determine the appropriate table(s) and context.
"""

        return prompt.strip()
