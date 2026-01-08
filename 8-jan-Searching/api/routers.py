from fastapi import APIRouter
from services.vector_service import ingest_pdf_service,search_service

router = APIRouter()

@router.post("/ingest-pdf")
def ingest_pdf(pdf_name: str):
    return ingest_pdf_service(pdf_name)

@router.get("/search")
def search(query: str, top_k: int = 3):
    return search_service(query, top_k)