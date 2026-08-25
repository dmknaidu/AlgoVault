from benchmarks.analyzer import compare_results
from benchmarks.models import BenchmarkResult


def create_result(
    algorithm_id: str,
    input_size: int,
    median_time: float,
) -> BenchmarkResult:
    return BenchmarkResult(
        algorithm_id=algorithm_id,
        input_size=input_size,
        runs=10,
        min_time=median_time,
        max_time=median_time,
        mean_time=median_time,
        median_time=median_time,
        environment="test",
    )


def test_compare_results():
    results = [
        create_result("linear_search", 100, 0.010),
        create_result("binary_search", 100, 0.001),
        create_result("linear_search", 1000, 0.100),
        create_result("binary_search", 1000, 0.002),
    ]

    comparisons = compare_results(
        results,
        "linear_search",
        "binary_search",
    )

    assert len(comparisons) == 2

    assert comparisons[0].input_size == 100
    assert comparisons[0].speedup == 10.0

    assert comparisons[1].input_size == 1000
    assert comparisons[1].speedup == 50.0


def test_compare_results_only_uses_common_sizes():
    results = [
        create_result("linear_search", 100, 0.010),
        create_result("linear_search", 1000, 0.100),
        create_result("binary_search", 100, 0.001),
    ]

    comparisons = compare_results(
        results,
        "linear_search",
        "binary_search",
    )

    assert len(comparisons) == 1
    assert comparisons[0].input_size == 100


def test_compare_results_empty():
    comparisons = compare_results(
        [],
        "linear_search",
        "binary_search",
    )

    assert comparisons == []