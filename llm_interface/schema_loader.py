# schema_loader.py
import os
import json

# Make sure these paths are correct relative to this script's location.
# Using os.path.abspath and os.path.dirname to make paths robust.
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
TABLE_NAMES_FILE = os.path.join(BASE_DIR, "table_name", "table_names.json")
TABLES_DIR = os.path.join(BASE_DIR, "Tables")  # Corrected folder name typo from 'Tabels' to 'Tables'

def load_table_names():
    with open(TABLE_NAMES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def load_table_schema(table_name):
    file_path = os.path.join(TABLES_DIR, f"{table_name}.json")
    if not os.path.exists(file_path):
        # Optional: raise error or log missing schema file
        print(f"Warning: Schema file for '{table_name}' not found at {file_path}")
        return None
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_schema_description():
    table_names = load_table_names()
    schema_descriptions = []

    for table in table_names:
        schema = load_table_schema(table)
        if not schema:
            continue

        table_desc = f"Table '{schema.get('table_name', table)}':\n"
        for col in schema.get("columns", []):
            col_line = f"- {col.get('column_name', 'Unknown')}: {col.get('description', 'No description')}"
            table_desc += col_line + "\n"
        schema_descriptions.append(table_desc)

    return "\n".join(schema_descriptions)

if __name__ == "__main__":
    description = generate_schema_description()
    print(description)
