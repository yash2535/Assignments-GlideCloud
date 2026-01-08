def test_ingest_pdf_success(client):
    response = client.post(
        "/ingest-pdf",
        params={"pdf_name": "AI.pdf"}
    )

    assert response.status_code == 200

    data = response.json()

    assert "chunks_created" in data
    assert data["chunks_created"] > 0
    assert data["status"] == "Embeddings stored on disk successfully"
