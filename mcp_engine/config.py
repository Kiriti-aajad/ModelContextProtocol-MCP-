"""Configuration constants for MCP Engine."""

from pathlib import Path

LOG_LEVEL: str = "INFO"

BASE_DIR: Path = Path(__file__).parent.resolve()

FAISS_INDEX_PATH: Path = BASE_DIR / "data" / "faiss_index.index"
FAISS_INDEX_DIM: int = 768

SCHEMA_PATH: Path = BASE_DIR / "data" / "schema.json"

# LLM client configuration placeholders
LLM_API_KEY: str = "your-llm-api-key"
LLM_MODEL_NAME: str = "gpt-4"

# Logging format
LOG_FORMAT: str = (
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
