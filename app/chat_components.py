# app/chat_components.py

from llm_interface.service import process_query

def get_llm_response(prompt: str):
    result = process_query(prompt)
    return result
