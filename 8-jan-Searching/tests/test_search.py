def test_search_returns_results(client):
    response = client.get(
        "/search",
        params={
            "query": "Explain AI",
            "top_k": 2
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "results" in data
    assert len(data["results"]) > 0

    result = data["results"][0]

    assert "chunk" in result
    assert "metadata" in result
    assert "similarity_score" in result
