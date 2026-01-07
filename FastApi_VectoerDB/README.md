**FastAPI Vector Database (Ollama + ChromaDB)**

This project is a FastAPI-based Vector Database service that stores and retrieves document and query embeddings using Ollama for embeddings and ChromaDB for vector storage.

It is designed as a learning + production-style foundation for semantic search and RAG (Retrieval-Augmented Generation) systems.

 **Features**

 FastAPI REST API

 Local embeddings using Ollama (no API keys)

 Persistent vector storage using ChromaDB

 Separate storage for:

 Document embeddings

Query embeddings

Debug endpoints to inspect stored vectors

Clean, modular project structure


**Run the Application**

From the project root:

uvicorn app.main:app --reload


Open Swagger UI:

http://127.0.0.1:8000/docs

 
**API Endpoints**
**Add Document**

POST /add-document

{
  "text": "FastAPI is a modern Python framework for building APIs"
}


Stores the document embedding in ChromaDB.

Search (and Store Query)

POST /search

{
  "query": "Python API framework",
  "top_k": 3
}


Stores the query embedding

Returns the most similar documents

 Debug Endpoints 
View Stored Documents


GET /debug/documents

Shows stored documents

Displays embedding preview (first 5 values)

View Stored Queries

GET /debug/queries

Shows stored queries

Displays embedding preview (first 5 values)