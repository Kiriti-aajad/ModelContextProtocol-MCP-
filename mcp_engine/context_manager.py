import os
import json

class ContextManager:
    def __init__(self, schema_path="data/database_schema.json"):
        self.schema_path = schema_path
        self.schema = {}
        self.table_names = set()
        self.column_to_tables = {}

        self._load_schema()

    def _load_schema(self):
        if not os.path.exists(self.schema_path):
            raise FileNotFoundError(f"Schema file not found: {self.schema_path}")

        with open(self.schema_path, 'r', encoding='utf-8') as f:
            self.schema = json.load(f)

        self._index_schema()

    def _index_schema(self):
        for full_table_name, columns in self.schema.items():
            self.table_names.add(full_table_name.lower())

            for col in columns:
                col_name = col.get("column_name", "").lower()
                if col_name:
                    if col_name not in self.column_to_tables:
                        self.column_to_tables[col_name] = set()
                    self.column_to_tables[col_name].add(full_table_name.lower())

    def list_all_tables(self):
        """Returns a list of all table names."""
        return sorted(list(self.table_names))

    def get_columns_in_table(self, table_name):
        """Returns column details for a given table."""
        return self.schema.get(table_name.lower(), [])

    def find_tables_with_column(self, column_name):
        """Returns a list of table names that contain the given column."""
        return sorted(list(self.column_to_tables.get(column_name.lower(), [])))

    def extract_context(self, query: str) -> dict:
        """
        Extracts relevant schema context based on query keywords (table and column names).
        Returns a dictionary with matched tables and their columns.
        """
        keywords = query.lower().split()
        matched_tables = set()
        matched_columns = set()

        # Find relevant tables and columns
        for word in keywords:
            if word in self.table_names:
                matched_tables.add(word)
            if word in self.column_to_tables:
                matched_columns.add(word)

        context = {}

        # Add tables directly matched
        for table in matched_tables:
            context[table] = self.get_columns_in_table(table)

        # Add tables indirectly matched via column references
        for column in matched_columns:
            tables = self.find_tables_with_column(column)
            for table in tables:
                if table not in context:
                    context[table] = self.get_columns_in_table(table)

        return context
