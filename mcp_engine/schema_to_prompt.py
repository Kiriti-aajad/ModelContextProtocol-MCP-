"""Converts database schema to natural language prompt snippets."""

from typing import Dict, Any, Optional, List

class SchemaToPrompt:
    def __init__(self, schema: Optional[Dict[str, Any]] = None):
        self.schema = schema or {}

    def convert(self) -> str:
        """
        Transform the schema dictionary into a human-readable prompt segment.

        Returns:
            A string describing tables and columns for LLM prompt context.
        """
        if not self.schema:
            return ""

        prompt_lines: List[str] = []
        for table_name, columns in self.schema.items():
            if isinstance(columns, list):
                cols_str = ", ".join(columns)
            else:
                cols_str = str(columns)
            prompt_lines.append(f"Table '{table_name}' contains columns: {cols_str}.")
        return "\n".join(prompt_lines)
