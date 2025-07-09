# backend/embed_utils.py

from sentence_transformers import SentenceTransformer

# Load the model once at startup
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def generate_embedding(text):
    return model.encode(text).tolist()

def batch_generate_embeddings(texts):
    return model.encode(texts, convert_to_numpy=True).tolist()

if __name__ == "__main__":
    sample_texts = [
        "Customer John Doe purchased 3 items for $89 on July 1st.",
        "Order 1023 was canceled due to payment failure."
    ]
    embeddings = batch_generate_embeddings(sample_texts)
    print(f"{len(embeddings)} embeddings generated. Vector size: {len(embeddings[0])}")
    for i, embedding in enumerate(embeddings):
        print(f"Embedding {i+1}: {embedding[:5]}...")  # Print first 5 dimensions for brevity