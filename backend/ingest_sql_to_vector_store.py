from db_utils import get_azure_sql_connection, fetch_data_as_text
from embed_utils import batch_generate_embeddings
from vector_store import FaissVectorStore

# 1. Connect to SQL and fetch data
conn = get_azure_sql_connection(
    server="b18sqlserver.database.windows.net",
    database="db-rag-poc",
    username="demouser",
    password="Changeme@123",
    driver="ODBC Driver 17 for SQL Server"
)
query = "SELECT TOP 100 * FROM SalesLT.Customer"
text_chunks = fetch_data_as_text(conn, query)

# 2. Embed the data
embeddings = batch_generate_embeddings(text_chunks)

# 3. Store in vector store
store = FaissVectorStore(dim=384, index_path="data/faiss.index", metadata_path="data/metadata.json")
store.add(embeddings, [{"text": t} for t in text_chunks])
store.save()
print("Ingestion complete.")