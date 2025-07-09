# RAG-POC: Azure SQL + RAG Assistant

This project demonstrates a **Retrieval-Augmented Generation (RAG)** pipeline using data from an Azure SQL database, vector search with FAISS, and local LLM inference (Ollama). The frontend is built with Streamlit, and the backend uses FastAPI.

---

## Features

- **Extracts data from Azure SQL** and converts it to text.
- **Embeds text** using Sentence Transformers.
- **Stores embeddings** and metadata in a FAISS vector store.
- **Retrieves relevant context** for user queries using vector similarity search.
- **Generates answers** using a local LLM (Ollama, e.g., Llama 3).
- **Interactive Streamlit UI** for asking questions.

---

## Project Structure

```
rag-poc/
│
├── backend/
│   ├── app.py              # FastAPI backend
│   ├── db_utils.py         # Azure SQL connection and data fetching
│   ├── embed_utils.py      # Embedding utilities
│   ├── vector_store.py     # FAISS vector store logic
│   ├── rag_pipeline.py     # RAG pipeline logic
│   ├── ingest_sql_to_vector_store.py  # Script to ingest SQL data into vector store
│   └── __init__.py
│
├── frontend/
│   └── app.py              # Streamlit UI
│
├── data/
│   ├── faiss.index         # FAISS index file (auto-generated)
│   └── metadata.json       # Metadata for each embedding (auto-generated)
│
└── README.md
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/rag-poc.git
cd rag-poc
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

You may also need:
```bash
pip install streamlit fastapi uvicorn faiss-cpu sentence-transformers pandas pyodbc ollama
```

### 3. Install and Start Ollama

- [Download Ollama](https://ollama.com/download) and install it.
- Pull the Llama 3 model:
  ```bash
  ollama pull llama3
  ```
- Start the Ollama server:
  ```bash
  ollama serve
  ```

### 4. Ingest Data from Azure SQL

Edit `backend/ingest_sql_to_vector_store.py` with your Azure SQL credentials, then run:

```bash
python backend/ingest_sql_to_vector_store.py
```

### 5. Start the Backend API

From the project root:

```bash
uvicorn backend.app:app --reload --port 8000
```

### 6. Start the Streamlit Frontend

```bash
streamlit run frontend/app.py
```

---

## Usage

- Open the Streamlit UI in your browser (usually at [http://localhost:8501](http://localhost:8501)).
- Enter your question and click "Ask".
- The system retrieves relevant context from your SQL data and generates an answer using the local LLM.

---

## Notes

- Make sure your Azure SQL credentials are correct and your IP is allowed in the Azure SQL firewall.
- Ollama must be running and the model pulled before asking questions.
- The vector store must be populated with data before querying.

---

## License

MIT License

---

## Acknowledgements

- [Ollama](https://ollama.com/)
- [Sentence Transformers](https://www.sbert.net/)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Streamlit](https://streamlit.io/)
- [FastAPI](https://fastapi.tiangolo.com/)
