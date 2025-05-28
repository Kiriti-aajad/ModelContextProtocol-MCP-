# mcp_engine/mcp_controller.py

from llm_interface.llm_client import call_llm_with_prompt
from database_layer.sql_query_generator import generate_sql_query
from database_layer.sql_query_validator import validate_sql
from database_layer.sql_executor import execute_query
from mcp_engine.response_formatter import format_response
from mcp_engine.context_manager import SessionContext

class MCPController:
    def __init__(self, db_path="data/tat_scores.db", model_name="gpt-3.5-turbo"):
        self.context = SessionContext()
        self.db_path = db_path
        self.model_name = model_name

    def process_user_query(self, user_query: str) -> dict:
        """
        Main function to handle user query: goes through LLM -> SQL -> DB -> Output
        Returns a dict with structured output and status.
        """
        try:
            # Step 1: Prepare prompt and call LLM
            llm_prompt = self.context.build_prompt(user_query)
            llm_response = call_llm_with_prompt(llm_prompt, model=self.model_name)
            
            # Step 2: Extract SQL query from LLM output
            sql_query = generate_sql_query(llm_response)

            # Step 3: Validate SQL
            if not validate_sql(sql_query):
                return {"status": "error", "message": "Invalid or unsafe SQL query."}

            # Step 4: Execute SQL query
            query_results = execute_query(sql_query, db_path=self.db_path)

            # Step 5: Format and return response
            formatted_output = format_response(query_results)

            return {
                "status": "success",
                "sql": sql_query,
                "results": formatted_output
            }

        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }
