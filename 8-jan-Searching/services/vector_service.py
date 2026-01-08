import os
import uuid
from datetime import datetime

from embeddings.embeddings import generate_embeddings
from vectordb.vector_client import documents_collection
from utils.pdf_loader import load_pdf_text
from utils.text_chunker import chunk_text


def ingest_pdf_service(pdf_name: str):
    
    pdf_path = f"data/{pdf_name}"


    if not os.path.exists(pdf_path):
        return {"error": "PDF not found"}

    # 1. Load PDF text
    text = load_pdf_text(pdf_path)

   
    chunks = chunk_text(
    text,
    max_chars=300,
    overlap_sentences=1
    )


    ids = []
    embeddings = []
    documents = []
    metadatas = []

    # 3. Create embedding per chunk
    for index, chunk in enumerate(chunks):
        ids.append(str(uuid.uuid4()))
        documents.append(chunk)
        embeddings.append(generate_embeddings(chunk))
        metadatas.append({
            "source": pdf_name,
            "chunk_index": index,
            "timestamp": datetime.utcnow().isoformat()
        })

    # 4. Store in ChromaDB (ON DISK)
    documents_collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )
  

    return {
        "pdf": pdf_name,
        "chunks_created": len(chunks),
        "status": "Embeddings stored on disk successfully"
    }
def search_service(query: str, top_k: int = 3):
    # 1. Create embedding for query
    query_embedding = generate_embeddings(query)

    # 2. Query ChromaDB
    results = documents_collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["documents", "metadatas", "distances"]
    )

    response = []

    for i in range(len(results["documents"][0])):
        distance = results["distances"][0][i]
        similarity_score = round(1 - distance, 4)

        response.append({
            "chunk": results["documents"][0][i],
            "metadata": results["metadatas"][0][i],
            "similarity_score": similarity_score
        })

    return {
        "query": query,
        "top_k": top_k,
        "results": response
    }