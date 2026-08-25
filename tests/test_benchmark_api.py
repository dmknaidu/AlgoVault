from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


def test_search_benchmark_endpoint():
    response = client.get("/api/benchmarks/search")

    assert response.status_code == 200

    data = response.json()

    assert data["algorithm"] == "search"
    assert data["count"] == 10
    assert len(data["results"]) == 10


def test_search_benchmark_result_structure():
    response = client.get("/api/benchmarks/search")

    assert response.status_code == 200

    result = response.json()["results"][0]

    assert "algorithm_id" in result
    assert "input_size" in result
    assert "runs" in result
    assert "min_time" in result
    assert "max_time" in result
    assert "mean_time" in result
    assert "median_time" in result
    assert "environment" in result

def test_search_benchmark_comparison():
    response = client.get(
        "/api/benchmarks/search/comparison",
        params={
            "algorithm_a": "linear_search",
            "algorithm_b": "binary_search",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["algorithm_a"] == "linear_search"
    assert data["algorithm_b"] == "binary_search"
    assert data["count"] == 5
    assert len(data["comparisons"]) == 5


def test_search_benchmark_comparison_requires_both_algorithms():
    response = client.get(
        "/api/benchmarks/search/comparison",
        params={
            "algorithm_a": "linear_search",
        },
    )

    assert response.status_code == 422