import json

def load_table_schema(json_path):
    """
    Load table schema from a JSON file.
    """
    try:
        with open(json_path, 'r') as file:
            schema = json.load(file)
        return schema
    except Exception as e:
        print(f"Failed to load schema from {json_path}: {e}")
        return None


def create_prompt(schema_json, table_name, user_question):
    """
    Construct an LLM prompt using the schema and user question.
    """
    if not schema_json:
        return "Schema could not be loaded."

    columns = []
    for col in schema_json:
        col_info = f"{col['column_name']} ({col['data_type']}"
        if col.get('max_length'):
            col_info += f", max_length={col['max_length']}"
        if col.get('is_nullable') == 'NO':
            col_info += ", NOT NULL"
        if col.get('is_identity'):
            col_info += ", Identity"
        if col.get('is_primary_key') == 'YES':
            col_info += ", Primary Key"
        col_info += ")"
        columns.append(col_info)

    schema_str = f"Table: {table_name}\nColumns:\n" + "\n".join(columns)

    prompt = f"""
You are a highly skilled SQL expert.
Based on the following table schema, generate a SQL SELECT query that answers the user's question.

{schema_str}

User question: {user_question}

Only provide the SQL query as output.
"""

    return prompt
