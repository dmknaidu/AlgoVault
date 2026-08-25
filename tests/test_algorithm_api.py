from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


def test_get_algorithms():
    response = client.get("/api/algorithms")

    assert response.status_code == 200

    data = response.json()

    assert data["count"] == 4
    assert len(data["algorithms"]) == 4


def test_algorithm_response_structure():
    response = client.get("/api/algorithms")

    assert response.status_code == 200

    algorithms = response.json()["algorithms"]

    for algorithm in algorithms:
        assert "id" in algorithm
        assert "name" in algorithm
        assert "category" in algorithm
        assert "description" in algorithm
        assert "time_complexity" in algorithm
        assert "space_complexity" in algorithm


def test_binary_search_metadata():
    response = client.get("/api/algorithms")

    algorithms = response.json()["algorithms"]

    binary_search = next(
        algorithm
        for algorithm in algorithms
        if algorithm["id"] == "binary_search"
    )

    assert binary_search["name"] == "Binary Search"
    assert binary_search["category"] == "Searching"
    assert binary_search["time_complexity"] == "O(log n)"
    assert binary_search["space_complexity"] == "O(1)"