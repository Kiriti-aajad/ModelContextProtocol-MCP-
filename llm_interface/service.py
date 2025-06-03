# llm_interface/service.py

import logging
from .embeddings.vector_store import VectorStore
from .llm.Client import LLMClient
from .query_engine.llm_query import QueryEngine
from . import config

logging.basicConfig(level=config.LOG_LEVEL)
logger = logging.getLogger(__name__)

# Initialize QueryEngine once
query_engine = QueryEngine(
    faiss_index_path=config.FAISS_INDEX_PATH,
    embedding_dim=config.FAISS_INDEX_DIM,
    snippets_path=r"E:\Github\ModelContextProtocol-MCP-\llm_interface\data\snippets.json"
)

def process_query(query: str):
    logger.info(f"Processing query: {query}")
    relevant_snippets = query_engine.get_relevant_snippets(query_engine.embed_query(query))
    sql_response = query_engine.generate_sql(query)
    logger.info("SQL generation successful.")
    return {
        "query": query,
        "relevant_tables": [snippet["table_name"] for snippet in relevant_snippets],
        "generated_sql": sql_response,
    }
