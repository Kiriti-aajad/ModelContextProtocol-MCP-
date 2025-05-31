import json
import os

def load_schema(path="database/database_schema.json"):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Schema file not found: {path}")
    
    with open(path, "r") as f:
        return json.load(f)
