import json
from pathlib import Path

from benchmarks.models import BenchmarkResult


def save_results(
    results: list[BenchmarkResult],
    file_path: str | Path,
) -> None:
    path = Path(file_path)

    path.parent.mkdir(parents=True, exist_ok=True)

    data = [
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
    ]

    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def load_results(
    file_path: str | Path,
) -> list[BenchmarkResult]:
    path = Path(file_path)

    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return [
        BenchmarkResult(
            algorithm_id=item["algorithm_id"],
            input_size=item["input_size"],
            runs=item["runs"],
            min_time=item["min_time"],
            max_time=item["max_time"],
            mean_time=item["mean_time"],
            median_time=item["median_time"],
            environment=item["environment"],
        )
        for item in data
    ]