import uuid
from datetime import datetime
from embeddings.ollama_embed import generate_embedding
from vectordb.chroma_client import (
    documents_collection,
    queries_collection
)


# ---------- DOCUMENT ----------

def add_document_service(text: str):
    doc_id = str(uuid.uuid4())
    embedding = generate_embedding(text)

    documents_collection.add(
        ids=[doc_id],
        documents=[text],
        embeddings=[embedding],
        metadatas=[{"type": "document"}]
    )

    return {
        "doc_id": doc_id,
        "status": "Document stored"
    }

# ---------- SEARCH ----------

def search_service(query: str, top_k: int):
    query_embedding = generate_embedding(query)
    query_id = str(uuid.uuid4())

    queries_collection.add(
        ids=[query_id],
        documents=[query],
        embeddings=[query_embedding],
        metadatas=[{
            "type": "query",
            "timestamp": datetime.utcnow().isoformat()
        }]
    )

    results = documents_collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return {
        "query_id": query_id,
        "query": query,
        "results": results["documents"][0]
    }

# ---------- DEBUG ----------

def get_documents_debug():
    data = documents_collection.get(
        include=["documents", "embeddings", "metadatas"]
    )

    embeddings = data["embeddings"] if data["embeddings"] is not None else []

    return {
        "count": len(data["ids"]),
        "documents": data["documents"],
        "embeddings_preview": [
            [float(x) for x in emb[:5]] for emb in embeddings
        ],
        "metadatas": data["metadatas"]
    }


def get_queries_debug():
    data = queries_collection.get(
        include=["documents", "embeddings", "metadatas"]
    )

    embeddings = data["embeddings"] if data["embeddings"] is not None else []

    return {
        "count": len(data["ids"]),
        "queries": data["documents"],
        "embeddings_preview": [
            [float(x) for x in emb[:5]] for emb in embeddings
        ],
        "metadatas": data["metadatas"]
    }
