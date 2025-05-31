import os
import json
from fastapi import FastAPI
from pydantic import BaseModel
from llm_interface.gpt2handler import GPT2Handler

# Adjust the path to your schema file
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "data", "database_schema.json")
with open(SCHEMA_PATH, "r") as f:
    db_schema = json.load(f)

llm = GPT2Handler()

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def process_query(request: QueryRequest):
    schema_str = json.dumps(db_schema, indent=2)
    prompt = (
        f"Given the following database schema:\n{schema_str}\n\n"
        f"Write an SQL query for: {request.query}"
    )
    response = llm.generate(prompt)
    return {"response": response}
@app.get("/")
async def root():
    return {"message": "Welcome to the MCP Server! Use the /query endpoint to process SQL queries."}