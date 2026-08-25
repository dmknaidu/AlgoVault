from pathlib import Path

from benchmarks.analyzer import compare_results
from benchmarks.storage import load_results


SEARCH_RESULTS_FILE = Path("data/benchmarks/search_experiment.json")


def get_search_benchmark_results():
    return load_results(SEARCH_RESULTS_FILE)


def compare_search_benchmarks(
    algorithm_a: str,
    algorithm_b: str,
):
    results = get_search_benchmark_results()

    return compare_results(
        results=results,
        algorithm_a=algorithm_a,
        algorithm_b=algorithm_b,
    )