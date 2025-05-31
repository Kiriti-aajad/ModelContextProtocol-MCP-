import os
from dotenv import load_dotenv
import pyodbc
import json  # <-- import json module

# Load environment variables from .env file
load_dotenv()

server = os.getenv("DB_SERVER")
database = os.getenv("DB_NAME")
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

# Build connection string for SQL Server Authentication
conn_str = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server};DATABASE={database};UID={username};PWD={password}"
)

def get_database_schema(connection):
    cursor = connection.cursor()

    # Get all tables (schema + name)
    cursor.execute("""
        SELECT TABLE_SCHEMA, TABLE_NAME
        FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_TYPE = 'BASE TABLE'
        ORDER BY TABLE_SCHEMA, TABLE_NAME
    """)
    tables = cursor.fetchall()

    schema = {}

    for schema_name, table_name in tables:
        # Get columns for the current table
        cursor.execute("""
            SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE, CHARACTER_MAXIMUM_LENGTH
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_SCHEMA = ? AND TABLE_NAME = ?
            ORDER BY ORDINAL_POSITION
        """, (schema_name, table_name))
        columns = cursor.fetchall()

        schema_key = f"{schema_name}.{table_name}"
        schema[schema_key] = []
        for col_name, data_type, is_nullable, char_max_len in columns:
            col_info = {
                "column_name": col_name,
                "data_type": data_type,
                "is_nullable": is_nullable,
                "max_length": char_max_len
            }
            schema[schema_key].append(col_info)

    return schema

def main():
    try:
        with pyodbc.connect(conn_str) as conn:
            print("Connected to database!")

            db_schema = get_database_schema(conn)

            # Print schema (optional)
            for table, columns in db_schema.items():
                print(f"\nTable: {table}")
                for col in columns:
                    max_len = col['max_length'] if col['max_length'] is not None else ''
                    print(f"  - {col['column_name']} ({col['data_type']}{f'({max_len})' if max_len else ''}) Nullable: {col['is_nullable']}")

            # Save schema to JSON file
            with open("database_schema.json", "w", encoding="utf-8") as f:
                json.dump(db_schema, f, indent=4)

            print("\nSchema saved to 'database_schema.json'")

    except Exception as e:
        print("Error connecting or fetching schema:", e)

if __name__ == "__main__":
    main()
