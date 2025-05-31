import streamlit as st
import re

st.set_page_config(page_title="ChatSQL", layout="centered")
st.markdown("## ChatSQL Assistant")
st.markdown("_Describe what SQL query you want in plain English._")

# Simulated available columns (you can connect to real DB schema later)
available_columns = [
    "customer_id", "customer_name", "order_id", "order_date",
    "order_amount", "product_name", "region", "sales_rep"
]

# --- Chat input ---
user_prompt = st.chat_input("What would you like to query?")

if user_prompt:
    # Display user's message
    st.chat_message("user").write(user_prompt)

    # Very basic logic to guess SELECT columns and WHERE conditions
    matched_columns = [col for col in available_columns if re.search(rf"\b{col}\b", user_prompt, re.IGNORECASE)]

    # Extract WHERE clause text (simple approach)
    filters = ""
    if "where" in user_prompt.lower():
        parts = user_prompt.lower().split("where")
        if len(parts) > 1:
            filters = parts[1].strip()

  
