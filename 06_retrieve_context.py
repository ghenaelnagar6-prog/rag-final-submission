import os
os.environ["ANONYMIZED_TELEMETRY"] = "False"

import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

client = chromadb.PersistentClient(path="./chroma_store")
collection = client.get_or_create_collection(name="first_aid_book")

def retrieve_context(query, n_results=3):
    query_embedding = model.encode([query]).tolist()
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=n_results
    )
    return results["documents"][0]

if __name__ == "__main__":
    test_question = "ma heya aarad al kasr"
    retrieved_chunks = retrieve_context(test_question)
    for i, chunk in enumerate(retrieved_chunks):
        print(f"--- Result {i+1} ---")
        print(chunk[:300])
