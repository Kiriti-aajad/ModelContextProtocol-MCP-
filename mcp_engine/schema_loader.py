"""Loads and validates JSON schema used for prompt construction."""

import json
from pathlib import Path
import logging
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

class SchemaLoader:
    def __init__(self, schema_path: Path):
        self.schema_path = schema_path
        self.schema: Optional[Dict[str, Any]] = None

    def load_schema(self) -> None:
        """
        Load schema JSON from disk and validate.

        Raises:
            FileNotFoundError: If schema file does not exist.
            json.JSONDecodeError: If JSON parsing fails.
        """
        logger.debug(f"Loading schema from {self.schema_path}")
        if not self.schema_path.exists():
            raise FileNotFoundError(f"Schema file not found: {self.schema_path}")

        with open(self.schema_path, "r", encoding="utf-8") as f:
            self.schema = json.load(f)
        logger.info(f"Schema loaded successfully from {self.schema_path}")

    def get_schema(self) -> Optional[Dict[str, Any]]:
        """
        Return the loaded schema, loading if not already loaded.

        Returns:
            The schema dictionary or None if not loaded.
        """
        if self.schema is None:
            self.load_schema()
        return self.schema
