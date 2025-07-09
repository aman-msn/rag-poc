# backend/rag_pipeline.py

import ollama
from backend.embed_utils import generate_embedding
from backend.vector_store import FaissVectorStore

def construct_prompt(context_chunks, user_query):
    # Safely extract text from dicts or use string directly
    context = "\n".join(
        chunk.get("text", str(chunk)) if isinstance(chunk, dict) else str(chunk)
        for chunk in context_chunks
    )
    prompt = f"""
You are an assistant that answers questions based on the following data:

{context}

Question: {user_query}
Answer:
"""
    return prompt

def query_rag_system(user_query, vector_store_path="data/faiss.index", metadata_path="data/metadata.json"):
    query_embedding = generate_embedding(user_query)
    
    # Load vector store
    store = FaissVectorStore(dim=384, index_path=vector_store_path, metadata_path=metadata_path)
    
    # Retrieve relevant chunks
    top_chunks = store.search(query_embedding, top_k=5)
    
    # Construct prompt
    prompt = construct_prompt(top_chunks, user_query)

    # For testing, mock a response (you can later plug in a local LLM or OpenAI)
    response = ollama.chat(model="llama3", messages=[
        {"role": "user", "content": prompt}
    ])
    answer = response['message']['content'].strip()
    return answer, prompt

if __name__ == "__main__":
    query = "How many customers are from the Company Name 'Many Bikes Store'?"
    response, prompt = query_rag_system(query)
    print("Prompt Sent to LLM:\n", prompt)
    print("\nLLM Response:\n", response)
# This script is a simple RAG pipeline that retrieves relevant context chunks from a vector store
# based on a user query, constructs a prompt, and returns a mock response.