from fastapi import FastAPI
from api.routers import router

app=FastAPI()

@app.get('/')
def greet():
    return "Searching in VectorDB implemented"
app.include_router(router)