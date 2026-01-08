import os
import csv
import chromadb

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROMA_DIR = os.path.join(BASE_DIR, "chroma_data")
COLLECTION_NAME = "pdf_chunks"
OUTPUT_CSV = os.path.join(BASE_DIR, "chroma_export.csv")

client = chromadb.PersistentClient(path=CHROMA_DIR)
collection = client.get_or_create_collection(name=COLLECTION_NAME)

print("Total documents:", collection.count())

data = collection.get(include=["documents", "embeddings", "metadatas"])

with open(OUTPUT_CSV, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "id",
        "document",
        "embedding_length",
        "embedding_first_10",
        "metadata"
    ])

    for i in range(len(data["ids"])):
        emb = data["embeddings"][i]
        writer.writerow([
            data["ids"][i],
            data["documents"][i],
            len(emb),
            emb[:10],
            data["metadatas"][i]
        ])

print("✅ CSV created:", OUTPUT_CSV)
