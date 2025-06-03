# llm_interface/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
from .service import process_query

app = FastAPI(title="Model Context Protocol - LLM Interface")

class QueryRequest(BaseModel):
    query: str

@app.get("/")
async def root():
    return {"message": "MCP LLM Interface is running."}

@app.post("/query")
async def query_database(request: QueryRequest):
    try:
        return process_query(request.query)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
