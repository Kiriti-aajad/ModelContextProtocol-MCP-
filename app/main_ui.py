import streamlit as st
import re

# Set page config
st.set_page_config(page_title="ChatSQL", layout="centered")

st.markdown("""
    <style>
        .chat-message {
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 1rem;
            max-width: 80%;
        }
        .user {
            background-color: #DCF8C6;
            align-self: flex-end;
        }
        .assistant {
            background-color: #F1F0F0;
            align-self: flex-start;
        }
        .chat-container {
            display: flex;
            flex-direction: column;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 ChatSQL Assistant")
st.markdown("Ask me SQL-style questions about your data. I’ll try to generate a query!")

# Simulated available columns (mock schema)
available_columns = [
    "customer_id", "customer_name", "order_id", "order_date",
    "order_amount", "product_name", "region", "sales_rep"
]

# --- Session State for Chat History ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Chat input ---
user_prompt = st.chat_input("What would you like to query?")

# --- Display Chat History ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(f'<div class="chat-message {msg["role"]}">{msg["content"]}</div>', unsafe_allow_html=True)

# --- Handle New Message ---
if user_prompt:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(f'<div class="chat-message user">{user_prompt}</div>', unsafe_allow_html=True)

    # Basic SQL building logic (for demo purposes)
    matched_columns = [col for col in available_columns if re.search(rf"\b{col}\b", user_prompt, re.IGNORECASE)]

    filters = ""
    if "where" in user_prompt.lower():
        parts = user_prompt.lower().split("where")
        if len(parts) > 1:
            filters = parts[1].strip()

    if matched_columns:
        sql_query = f"SELECT {', '.join(matched_columns)} FROM your_table"
        if filters:
            sql_query += f" WHERE {filters}"
        sql_query += ";"
    else:
        sql_query = "Sorry, I couldn't identify any relevant columns from your input."

    # Save assistant message
    st.session_state.messages.append({"role": "assistant", "content": sql_query})
    with st.chat_message("assistant"):
        st.markdown(f'<div class="chat-message assistant">{sql_query}</div>', unsafe_allow_html=True)
