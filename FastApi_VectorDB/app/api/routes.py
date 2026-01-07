from fastapi import APIRouter
from app.api.services.vector_service import (
    add_document_service,
    search_service,
    get_documents_debug,
    get_queries_debug
)


router = APIRouter()

@router.post("/add-document")
def add_document(text: str):
    return add_document_service(text)


@router.post("/search")
def search(query: str, top_k: int = 3):
    return search_service(query, top_k)


@router.get("/debug/documents")
def debug_documents():
    return get_documents_debug()


@router.get("/debug/queries")
def debug_queries():
    return get_queries_debug()
