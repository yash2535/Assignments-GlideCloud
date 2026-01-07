import chromadb
from chromadb.config import Settings

client = chromadb.Client(
    Settings(
        persist_directory="chroma_data"
    )
)

documents_collection = client.get_or_create_collection(
    name="documents"
)

queries_collection = client.get_or_create_collection(
    name="queries"
)
