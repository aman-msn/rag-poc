# backend/vector_store.py

import faiss
import numpy as np
import json
import os

class FaissVectorStore:
    def __init__(self, dim, index_path="data/faiss.index", metadata_path="data/metadata.json"):
        self.index_path = index_path
        self.metadata_path = metadata_path
        self.dim = dim
        self.index = faiss.IndexFlatL2(dim)
        self.metadata = []

        # Load existing index if available
        if os.path.exists(index_path):
            self.index = faiss.read_index(index_path)
        if os.path.exists(metadata_path):
            with open(metadata_path, "r") as f:
                self.metadata = json.load(f)

    def add(self, embeddings, metadata_list):
        vectors = np.array(embeddings).astype("float32")
        self.index.add(vectors)
        self.metadata.extend(metadata_list)
        self._save()

    def search(self, query_embedding, top_k=5):
        query = np.array([query_embedding]).astype("float32")
        distances, indices = self.index.search(query, top_k)
        results = []
        for i in indices[0]:
            if i < len(self.metadata):
                results.append(self.metadata[i])
        return results

    def _save(self):
        faiss.write_index(self.index, self.index_path)
        with open(self.metadata_path, "w") as f:
            json.dump(self.metadata, f, indent=2)

    def save(self):
        """
        Public method to save the FAISS index and metadata to disk.
        """
        faiss.write_index(self.index, self.index_path)
        with open(self.metadata_path, "w") as f:
            json.dump(self.metadata, f, indent=2)


if __name__ == "__main__":
    # Example usage
    vector_store = FaissVectorStore(dim=384)  # Assuming 384-dimensional embeddings

    # Add some sample data
    sample_embeddings = [[0.1] * 384, [0.2] * 384]
    sample_metadata = [{"text": "Sample 1"}, {"text": "Sample 2"}]
    vector_store.add(sample_embeddings, sample_metadata)

    # Search for similar items
    query_embedding = [0.01303942967206239] * 384
    results = vector_store.search(query_embedding, top_k=2)
    print("Search Results:", results)