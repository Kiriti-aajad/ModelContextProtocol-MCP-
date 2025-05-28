import streamlit as st
import pandas as pd

available_columns = [
    "customer_id",
    "customer_name",
    "order_id",
    "order_date",
    "order_amount",
    "product_name",
    "region",
    "sales_rep",
]

st.title("Dynamic SQL Query Builder - Add Columns & Filters")

# Initialize session state list for selected columns
if "selected_columns" not in st.session_state:
    st.session_state.selected_columns = []

col1, col2 = st.columns([2, 3])

with col1:
    st.header("Step 1: Add Columns")

    # Dropdown to select a column to add
    col_to_add = st.selectbox(
        "Select column to add:",
        options=[c for c in available_columns if c not in st.session_state.selected_columns]
    )

    if st.button("Add Column"):
        if col_to_add and col_to_add not in st.session_state.selected_columns:
            st.session_state.selected_columns.append(col_to_add)

    if st.session_state.selected_columns:
        st.write("### Selected Columns Table")
        df_cols = pd.DataFrame(st.session_state.selected_columns, columns=["Column Name"])
        st.table(df_cols)
    else:
        st.info("No columns added yet.")

    # Button to clear all selected columns
    if st.session_state.selected_columns and st.button("Clear All Columns"):
        st.session_state.selected_columns = []

with col2:
    st.header("Step 2: Additional Commands / Filters")
    filter_conditions = st.text_area(
        "Enter any filter conditions or commands:",
        placeholder="e.g., order_amount > 1000 AND region = 'East'",
        height=150,
    )

st.markdown("---")
st.header("Query Preview")

if st.session_state.selected_columns:
    columns_str = ", ".join(st.session_state.selected_columns)
else:
    columns_str = "*"

sql_preview = f"SELECT {columns_str} FROM your_table"

if filter_conditions.strip():
    sql_preview += f" WHERE {filter_conditions.strip()}"

st.code(sql_preview, language="sql")

st.markdown("---")
st.header("Debug Info")

st.write("Selected Columns:", st.session_state.selected_columns)
st.write("Additional Commands / Filters:", filter_conditions)
