from mcp_engine.schema_loader import load_schema as SchemaLoader
from mcp_engine.context_manager import ContextManager
from mcp_engine.prompt_handler import PromptHandler
from mcp_engine.response_formatter import ResponseFormatter

class MCPController:
    def __init__(self, schema_path="schemas/db_schema.json"):
        self.schema_loader = SchemaLoader(schema_path)
        self.context_manager = ContextManager(self.schema_loader)
        self.prompt_handler = PromptHandler(self.context_manager)
        self.response_formatter = ResponseFormatter()

    def process_query(self, query: str) -> dict:
        # Step 1: Get relevant context from the schema
        context = self.context_manager.extract_context(query)

        # Step 2: Build a prompt (in a real case this would go to an LLM)
        prompt = self.prompt_handler.build_prompt(query)

        # Simulate LLM response (you can replace this with actual LLM call)
        raw_response = f"[Simulated Answer] You asked: '{query}'\n\n{prompt}"

        # Step 3: Format response
        final_output = self.response_formatter.format(raw_response)
        return final_output
