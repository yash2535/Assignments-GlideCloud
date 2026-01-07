from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Ollama + Chroma Vector API")

app.include_router(router)
