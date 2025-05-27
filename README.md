# ModelContextProtocol-MCP-
GOAL -> To create an MCP server with LLM  to connect with database  and retrive data from Multiple tables and create a final output table by sql script or retrive some information.


MCP_Project/
│
├── app/                          # Streamlit or Web UI frontend
│   ├── main_ui.py                # Streamlit-based UI with input box, results panel
│   ├── chat_components.py        # Chat history, message formatting, input handling
│   └── config.py                 # Frontend configs (API keys, UI settings, etc.)
│
├── mcp_engine/                   # Core protocol engine to handle LLM ↔ DB ↔ Response
│   ├── mcp_controller.py         # Controls flow between UI ↔ LLM ↔ SQL ↔ DB
│   ├── prompt_handler.py         # Prepares and processes LLM prompts
│   ├── response_formatter.py     # Post-processes DB output to table, JSON, etc.
│   └── context_manager.py        # Maintains session context (user queries, table info)
│
├── llm_interface/                # LLM abstraction (can support GPT, Ollama, etc.)
│   ├── llm_client.py             # Sends/receives prompt to/from local or API-based LLM
│   └── prompt_templates.py       # Predefined prompt patterns for SQL generation, filtering
│
├── database_layer/               # Handles SQL generation, validation, execution
│   ├── sql_query_generator.py    #  Generates SQL queries from LLM text
│   ├── sql_query_validator.py    #  Validates and sanitizes SQL queries
│   ├── sql_executor.py           # Executes validated queries on the database
│   └── db_connector.py           # Connects to DB (SQLite, PostgreSQL, etc.)
│
├── data/                         # Example or production datasets
│   ├── tat_scores.csv            # Sample data file
│   └── schema.json               # JSON schema for DB tables
│
├── tests/                        # Unit and integration tests
│   ├── test_sql_generation.py
│   ├── test_llm_responses.py
│   └── test_validator.py
│
├── logs/                         # Query logs, error logs, etc.
│   └── mcp_app.log
│
├── requirements.txt              # Python dependencies
├── README.md                     # Project overview and setup
└── run.py                        # Entry point to launch the app
