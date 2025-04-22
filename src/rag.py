import faiss
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def encode_and_index(text_list):
    embeddings = model.encode(text_list)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index, embeddings

def retrieve(query, index, corpus_embeddings, corpus, k=3):
    query_embedding = model.encode([query])
    distances, indices = index.search(query_embedding, k)
    return [corpus[idx] for idx in indices[0]]

if __name__ == "__main__":
    corpus = ["patient has diabetes", "patient has hypertension", "normal glucose levels"]
    index, embeddings = encode_and_index(corpus)
    results = retrieve("high blood sugar", index, embeddings, corpus)
    print(results)
