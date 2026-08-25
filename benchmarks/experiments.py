from collections.abc import Callable
from typing import Any

from benchmarks.models import BenchmarkResult
from benchmarks.runner import run_benchmark


def run_experiment(
    algorithm_id: str,
    function: Callable[..., Any],
    input_sizes: list[int],
    input_builder: Callable[[int], tuple[Any, ...]],
    runs: int,
    environment: str = "local",
) -> list[BenchmarkResult]:
    results: list[BenchmarkResult] = []

    for input_size in input_sizes:
        args = input_builder(input_size)

        result = run_benchmark(
            algorithm_id=algorithm_id,
            function=function,
            args=args,
            input_size=input_size,
            runs=runs,
            environment=environment,
        )

        results.append(result)

    return results