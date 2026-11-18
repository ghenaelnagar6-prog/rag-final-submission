import re
from sentence_transformers import SentenceTransformer
import numpy as np

with open("chunks.txt", "r", encoding="utf-8") as f:
    raw_chunks_file = f.read()

parts = re.split(r"--- Chunk \d+ ---\n", raw_chunks_file)
chunks = [p.strip() for p in parts if p.strip() != ""]

print(f"Total chunks loaded: {len(chunks)}")

model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
embeddings = model.encode(chunks, show_progress_bar=True)

print(f"Number of embeddings: {len(embeddings)}")
print(f"Embedding dimension: {len(embeddings[0])}")

np.save("embeddings.npy", embeddings)
print("Saved embeddings.npy successfully!")
