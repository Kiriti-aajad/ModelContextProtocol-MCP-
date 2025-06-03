import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from mcp_engine.mcp_controller import MCPController
from mcp_engine.context_manager import ContextManager
from mcp_engine.prompt_handler import PromptHandler
from mcp_engine.response_formatter import ResponseFormatter

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Model Context Protocol Engine")

# Initialize MCPController with components (replace with actual LLMClient)
mcp_controller = MCPController(
    context_manager=ContextManager(),
    prompt_handler=PromptHandler(),
    response_formatter=ResponseFormatter(),
    llm_client=None,  # TODO: Replace with your LLM client instance
)

class QueryRequest(BaseModel):
    user_id: str
    query: str

class QueryResponse(BaseModel):
    response: str

@app.post("/query", response_model=QueryResponse)
async def handle_query(request: QueryRequest):
    logger.info(f"Received query from user_id={request.user_id}: {request.query}")
    try:
        response_text = mcp_controller.handle_query(request.user_id, request.query)
        logger.info("Query processed successfully.")
        return QueryResponse(response=response_text)
    except Exception as e:
        logger.error(f"Error processing query: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))
