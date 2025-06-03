import json

def load_schema_snippets(snippets_path):
    with open(snippets_path, "r", encoding="utf-8") as f:
        snippets = json.load(f)
    return snippets
