# backend/db_utils.py

import pyodbc
import pandas as pd

def get_azure_sql_connection(server, database, username, password, driver="ODBC Driver 17 for SQL Server"):
    connection_string = f"""
        DRIVER={{{driver}}};
        SERVER=b18sqlserver.database.windows.net;
        DATABASE=db-rag-poc;
        UID=demouser;
        PWD=$yn@pse@2025;
        Encrypt=yes;
        TrustServerCertificate=no;
        Connection Timeout=30;
    """
    conn = pyodbc.connect(connection_string)
    # Check if the connection was successful
    print("Available ODBC Drivers:", pyodbc.drivers())
    if conn is None:
        raise Exception("Failed to connect to the database.")
    return conn

def fetch_data_as_text(conn, query):
    df = pd.read_sql(query, conn)
    # Convert rows into readable text chunks
    text_data = []
    for _, row in df.iterrows():
        row_text = "; ".join([f"{col}: {val}" for col, val in row.items()])
        text_data.append(row_text)
    return text_data

if __name__ == "__main__":
    server = "your-server.database.windows.net"
    database = "your-db"
    username = "your-username"
    password = "your-password"

    conn = get_azure_sql_connection(server, database, username, password)
    query = "Select TOP 100 * from SalesLT.Customer"
    text_chunks = fetch_data_as_text(conn, query)

    for chunk in text_chunks[:5]:
        print(chunk)
