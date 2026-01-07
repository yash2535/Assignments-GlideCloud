import ollama

def generate_embedding(text: str):
    response = ollama.embeddings(
        model="mxbai-embed-large:latest",
        prompt=text
    )
    return response["embedding"]
