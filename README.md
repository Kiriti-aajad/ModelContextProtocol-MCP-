# 🧐 ModelContextProtocol (MCP)

## 🚀 Goal

The **ModelContextProtocol (MCP)** project aims to build a flexible and modular system that connects a Large Language Model (LLM) with structured databases. The LLM interprets user queries, generates SQL scripts, retrieves data from multiple tables, and returns the final output in a structured format (e.g., tables, charts, summaries).

---

## 📁 Project Structure

```
MCP_Project/
│
├── app/                          # Frontend: Streamlit-based user interface
│   ├── main_ui.py                # Main UI with input box, result panel, interaction logic
│   ├── chat_components.py        # Chat message formatting and chat history
│   └── config.py                 # UI and frontend configuration (API keys, styles)
│
├── mcp_engine/                   # MCP Core engine managing full flow
│   ├── mcp_controller.py         # Orchestrates flow: UI ↔ LLM ↔ SQL ↔ DB ↔ Response
│   ├── prompt_handler.py         # Formats and handles LLM prompt construction
│   ├── response_formatter.py     # Formats DB output to JSON, table, etc.
│   └── context_manager.py        # Manages session context and table/query history
│
├── llm_interface/                # Handles LLM API or local call integration
│   ├── llm_client.py             # Sends queries to LLMs (GPT, Ollama, etc.)
│   └── prompt_templates.py       # Template prompts for different query types
│
├── database_layer/               # Responsible for SQL generation and DB interaction
│   ├── sql_query_generator.py    # 🔹 Converts text to SQL query
│   ├── sql_query_validator.py    # 🔒 Ensures SQL is valid and secure
│   ├── sql_executor.py           # 🧠 Executes SQL queries on target DB
│   └── db_connector.py           # 📡 Establishes connection to DB (e.g., SQLite, Postgres)
│
├── data/                         # Demo or production datasets
│   ├── tat_scores.csv            # Example financial dataset
│   └── schema.json               # Schema definitions for table columns and types
│
├── tests/                        # Unit and integration tests
│   ├── test_sql_generation.py
│   ├── test_llm_responses.py
│   └── test_validator.py
│
├── logs/                         # Logging system
│   └── mcp_app.log               # Log file for errors, queries, sessions
│
├── requirements.txt              # Python package dependencies
├── README.md                     # Project documentation (this file)
└── run.py                        # 🚀 Entry point to launch the MCP app
```

---

## 🤩 Features

* ✅ Seamless integration with local or API-based LLMs
* 🧠 Smart SQL generation from natural language queries
* 🔐 Query validation and sanitation for secure database access
* 📊 Real-time data retrieval and response formatting
* 💬 Chat-style UI for query history and interaction
* 🔀 Multi-table joins, filter application, and conditional logic

---

## 💻 Getting Started

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourname/ModelContextProtocol-MCP.git
   cd ModelContextProtocol-MCP
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**

   ```bash
   python run.py
   ```

---

## 🤪 Testing

Run all tests using:

```bash
pytest tests/
```

---

## 📘 Example Use Case

> **Query:** "Show me the average TAT score of enterprises with more than 100 employees, grouped by sector."
>
> **MCP Flow:**
>
> 1. LLM parses the question and generates a SQL query.
> 2. Query is validated and executed on the database.
> 3. Results are formatted into a table and displayed in the chat UI.

---

## 📬 Contact

For questions or contributions, feel free to reach out or create a pull request!

---

## 📄 License

MIT License. See `LICENSE` for details.
