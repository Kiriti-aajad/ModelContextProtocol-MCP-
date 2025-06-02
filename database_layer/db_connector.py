import os
import pyodbc
from dotenv import load_dotenv
from pathlib import Path

# Get path to .env in root folder (1 level up from this file)
env_path = Path(__file__).resolve().parents[1] / '.env'

# Load environment variables from the .env file
load_dotenv(dotenv_path=env_path)

def connect_to_mssql():
    server = os.getenv('DB_SERVER')
    database = os.getenv('DB_NAME')
    username = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')

    if not all([server, database, username, password]):
        print("One or more environment variables are missing.")
        return None

    try:
        conn_str = (
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'UID={username};'
            f'PWD={password};'
            'TrustServerCertificate=yes;'
        )
        conn = pyodbc.connect(conn_str, timeout=5)
        print("Connected to MSSQL successfully!")
        return conn  # Return the live connection object

    except Exception as e:
        print("Failed to connect to MSSQL database:")
        print(str(e))
        return None

if __name__ == "__main__":
    # Example usage: just to test connection
    connection = connect_to_mssql()
    if connection:
        connection.close()
