import pytest

from benchmarks.runner import run_benchmark


def test_run_benchmark_returns_result():
    def add_numbers(a: int, b: int) -> int:
        return a + b

    result = run_benchmark(
        algorithm_id="test_add",
        function=add_numbers,
        args=(1, 2),
        input_size=1,
        runs=5,
    )

    assert result.algorithm_id == "test_add"
    assert result.input_size == 1
    assert result.runs == 5
    assert result.min_time >= 0
    assert result.max_time >= result.min_time
    assert result.mean_time >= result.min_time
    assert result.mean_time <= result.max_time
    assert result.median_time >= result.min_time
    assert result.median_time <= result.max_time


def test_run_benchmark_supports_multiple_arguments():
    def multiply(a: int, b: int) -> int:
        return a * b

    result = run_benchmark(
        algorithm_id="test_multiply",
        function=multiply,
        args=(6, 7),
        input_size=1,
        runs=3,
    )

    assert result.runs == 3


def test_run_benchmark_rejects_negative_input_size():
    with pytest.raises(ValueError):
        run_benchmark(
            algorithm_id="test",
            function=lambda: None,
            args=(),
            input_size=-1,
            runs=5,
        )


def test_run_benchmark_rejects_zero_runs():
    with pytest.raises(ValueError):
        run_benchmark(
            algorithm_id="test",
            function=lambda: None,
            args=(),
            input_size=10,
            runs=0,
        )


def test_run_benchmark_rejects_negative_runs():
    with pytest.raises(ValueError):
        run_benchmark(
            algorithm_id="test",
            function=lambda: None,
            args=(),
            input_size=10,
            runs=-1,
        )