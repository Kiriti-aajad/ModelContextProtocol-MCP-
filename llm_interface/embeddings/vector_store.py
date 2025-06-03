from llm_interface.embeddings.faiss_index import load_faiss_index
import numpy as np

class VectorStore:
    def __init__(self, faiss_index_path, snippets, embedding_dim):
        self.index, self.embeddings = load_faiss_index(faiss_index_path)
        self.snippets = snippets
        self.embedding_dim = embedding_dim

    def query(self, query_embedding, top_k=5):
        distances, indices = self.index.search(np.array([query_embedding]), top_k)
        return indices[0], distances[0]
