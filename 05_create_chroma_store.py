import os
os.environ["ANONYMIZED_TELEMETRY"] = "False"

import re
import numpy as np
import chromadb

with open("chunks.txt", "r", encoding="utf-8") as f:
    raw_chunks_file = f.read()

parts = re.split(r"--- Chunk \d+ ---\n", raw_chunks_file)
chunks = [p.strip() for p in parts if p.strip() != ""]

embeddings = np.load("embeddings.npy")

print(f"Loaded {len(chunks)} chunks and {len(embeddings)} embeddings")

client = chromadb.PersistentClient(path="./chroma_store")
collection = client.get_or_create_collection(name="first_aid_book")

ids = [f"chunk_{i}" for i in range(len(chunks))]

collection.add(
    documents=chunks,
    embeddings=embeddings.tolist(),
    ids=ids
)

print(f"Total items stored in Chroma: {collection.count()}")
