import os
from dotenv import load_dotenv

load_dotenv()  # loads .env from root folder

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
EMBEDDINGS_PATH = os.getenv("EMBEDDINGS_PATH", r"E:\Github\ModelContextProtocol-MCP-\llm_interface\data\embeddings.npy")
FAISS_INDEX_PATH = os.getenv("FAISS_INDEX_PATH", r"E:\Github\ModelContextProtocol-MCP-\llm_interface\data\faiss.index")  # note: no underscore
SNIPPETS_PATH = os.getenv("SNIPPETS_PATH", r"E:\Github\ModelContextProtocol-MCP-\llm_interface\data\snippets.json")

FAISS_INDEX_DIM = int(os.getenv("FAISS_INDEX_DIM", 1536))
MAX_QUERY_RESULTS = int(os.getenv("MAX_QUERY_RESULTS", 5))
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
