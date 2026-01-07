from fastapi import APIRouter
from embeddings.ollama_embed import generate_embedding
from vectordb.chroma_client import (
    documents_collection,
    queries_collection
)
import uuid
from datetime import datetime

router = APIRouter()

@router.post("/add-document")
def add_document(text: str):
    doc_id = str(uuid.uuid4())
    embedding = generate_embedding(text)

    documents_collection.add(
        ids=[doc_id],
        documents=[text],
        embeddings=[embedding],
        metadatas=[{"type": "document"}]
    )

    return {"doc_id": doc_id, "status": "Document stored"}

@router.post("/search")
def search(query: str, top_k: int = 3):
    query_embedding = generate_embedding(query)
    query_id = str(uuid.uuid4())

    # store query embedding
    queries_collection.add(
        ids=[query_id],
        documents=[query],
        embeddings=[query_embedding],
        metadatas=[{
            "type": "query",
            "timestamp": datetime.utcnow().isoformat()
        }]
    )

    # search documents
    results = documents_collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return {
        "query_id": query_id,
        "query": query,
        "results": results["documents"][0]
    }


@router.get("/debug/documents")
def print_documents():
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



@router.get("/debug/queries")
def print_queries():
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

