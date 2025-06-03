import faiss
import numpy as np
from llm_interface.config import EMBEDDINGS_PATH


def load_faiss_index(faiss_index_path):
    index = faiss.read_index(faiss_index_path)
    embeddings = np.load(EMBEDDINGS_PATH)
    return index, embeddings
