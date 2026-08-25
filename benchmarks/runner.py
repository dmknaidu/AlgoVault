import statistics
import time
from collections.abc import Callable
from typing import Any

from benchmarks.models import BenchmarkResult


def run_benchmark(
    algorithm_id: str,
    function: Callable[..., Any],
    args: tuple[Any, ...],
    input_size: int,
    runs: int,
    environment: str = "local",
) -> BenchmarkResult:
    if input_size < 0:
        raise ValueError("input_size must be non-negative")

    if runs <= 0:
        raise ValueError("runs must be greater than zero")

    timings: list[float] = []

    for _ in range(runs):
        start = time.perf_counter()

        function(*args)

        elapsed = time.perf_counter() - start
        timings.append(elapsed)

    return BenchmarkResult(
        algorithm_id=algorithm_id,
        input_size=input_size,
        runs=runs,
        min_time=min(timings),
        max_time=max(timings),
        mean_time=statistics.mean(timings),
        median_time=statistics.median(timings),
        environment=environment,
    )