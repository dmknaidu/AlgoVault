from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.algorithm_service import get_all_algorithms
from backend.benchmark_service import (
    compare_search_benchmarks,
    get_search_benchmark_results,
)

app = FastAPI(
    title="AlgoVault API",
    description="Intelligent Algorithm & Data Structure Engine",
    version="0.1.0",
)

@app.get("/api/algorithms")
def get_algorithms():
    algorithms = get_all_algorithms()

    return {
        "count": len(algorithms),
        "algorithms": [
            {
                "id": algorithm.id,
                "name": algorithm.name,
                "category": algorithm.category,
                "description": algorithm.description,
                "time_complexity": algorithm.time_complexity,
                "space_complexity": algorithm.space_complexity,
            }
            for algorithm in algorithms
        ],
    }
    
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://localhost:5175",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174",
        "http://127.0.0.1:5175",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "name": "AlgoVault",
        "message": "Intelligent Algorithm & Data Structure Engine",
        "version": "0.1.0",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "algovault-api",
    }

@app.get("/api/benchmarks/search")
def get_search_benchmarks():
    results = get_search_benchmark_results()

    return {
        "algorithm": "search",
        "count": len(results),
        "results": [
            {
                "algorithm_id": result.algorithm_id,
                "input_size": result.input_size,
                "runs": result.runs,
                "min_time": result.min_time,
                "max_time": result.max_time,
                "mean_time": result.mean_time,
                "median_time": result.median_time,
                "environment": result.environment,
            }
            for result in results
        ],
    }

@app.get("/api/benchmarks/search/comparison")
def get_search_benchmark_comparison(
    algorithm_a: str,
    algorithm_b: str,
):
    comparisons = compare_search_benchmarks(
        algorithm_a=algorithm_a,
        algorithm_b=algorithm_b,
    )

    if not comparisons:
        raise HTTPException(
            status_code=404,
            detail="No comparable benchmark results found",
        )

    return {
        "algorithm_a": algorithm_a,
        "algorithm_b": algorithm_b,
        "count": len(comparisons),
        "comparisons": [
            {
                "input_size": comparison.input_size,
                "algorithm_a_time": comparison.algorithm_a_time,
                "algorithm_b_time": comparison.algorithm_b_time,
                "speedup": comparison.speedup,
            }
            for comparison in comparisons
        ],
    }