import pytest

from benchmarks.models import BenchmarkResult


def test_benchmark_result_creation():
    result = BenchmarkResult(
        algorithm_id="linear_search",
        input_size=10000,
        runs=20,
        min_time=0.0001,
        max_time=0.0003,
        mean_time=0.00018,
        median_time=0.00017,
        environment="local",
    )

    assert result.algorithm_id == "linear_search"
    assert result.input_size == 10000
    assert result.runs == 20
    assert result.median_time == 0.00017
    assert result.environment == "local"


def test_benchmark_result_is_immutable():
    result = BenchmarkResult(
        algorithm_id="linear_search",
        input_size=100,
        runs=10,
        min_time=0.001,
        max_time=0.002,
        mean_time=0.0015,
        median_time=0.0014,
        environment="local",
    )

    with pytest.raises(AttributeError):
        result.input_size = 200