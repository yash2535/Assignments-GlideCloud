import os
import chromadb
from chromadb.config import Settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROMA_DIR = os.path.join(BASE_DIR, "chroma_data")

client = chromadb.Client(
    Settings(
        persist_directory=CHROMA_DIR
    )
)

documents_collection = client.get_or_create_collection(
    name="pdf_chunks"
)
