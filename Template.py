import os

# Define the folder and file structure
project_structure = {
    "app": [
        "main_ui.py",
        "chat_components.py",
        "config.py"
    ],
    "mcp_engine": [
        "mcp_controller.py",
        "prompt_handler.py",
        "response_formatter.py",
        "context_manager.py"
    ],
    "llm_interface": [
        "llm_client.py",
        "prompt_templates.py"
    ],
    "database_layer": [
        "sql_query_generator.py",
        "sql_query_validator.py",
        "sql_executor.py",
        "db_connector.py"
    ],
    "data": [
        "tat_scores.csv",
        "schema.json"
    ],
    "tests": [
        "test_sql_generation.py",
        "test_llm_responses.py",
        "test_validator.py"
    ],
    "logs": [
        "mcp_app.log"
    ]
}

# Additional root-level files
root_files = ["requirements.txt", "run.py"]

def create_structure():
    for folder, files in project_structure.items():
        os.makedirs(folder, exist_ok=True)
        for file in files:
            file_path = os.path.join(folder, file)
            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    f.write("")  # create empty file
    for file in root_files:
        if not os.path.exists(file):
            with open(file, "w") as f:
                f.write("")  # create empty file

    print("✅ MCP project structure created successfully.")

if __name__ == "__main__":
    create_structure()
