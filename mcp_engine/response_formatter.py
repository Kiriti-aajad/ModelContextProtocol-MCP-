# mcp_engine/response_formatter.py

import pandas as pd

def format_response(query_result: dict) -> dict:
    """
    Converts raw DB query output to a structured JSON-like dictionary.
    
    query_result should be a dict:
    {
        "columns": [...],
        "rows": [...]
    }
    """
    if not query_result or not query_result.get("rows"):
        return {
            "message": "No results found.",
            "data": [],
            "columns": []
        }

    df = pd.DataFrame(query_result["rows"], columns=query_result["columns"])
    json_data = df.to_dict(orient="records")

    return {
        "message": "Query successful.",
        "columns": query_result["columns"],
        "data": json_data
    }
