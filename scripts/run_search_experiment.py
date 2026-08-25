from pathlib import Path

from algorithms.catalog import registry
from benchmarks.experiments import run_experiment
from benchmarks.generators import generate_sorted_array
from benchmarks.models import BenchmarkResult
from benchmarks.storage import save_results


INPUT_SIZES = [10, 100, 1_000, 10_000, 100_000]
RUNS = 20

OUTPUT_FILE = Path("data/benchmarks/search_experiment.json")


def build_search_input(size: int) -> tuple[list[int], int]:
    items = generate_sorted_array(size)
    target = items[-1]

    return items, target


def print_results(
    linear_results: list[BenchmarkResult],
    binary_results: list[BenchmarkResult],
) -> None:
    print("Search Algorithm Experiment")
    print("=" * 80)
    print(
        f"{'Input Size':>12} "
        f"{'Linear Median (ms)':>22} "
        f"{'Binary Median (ms)':>22}"
    )
    print("-" * 80)

    for linear, binary in zip(linear_results, binary_results):
        linear_ms = linear.median_time * 1000
        binary_ms = binary.median_time * 1000

        print(
            f"{linear.input_size:>12} "
            f"{linear_ms:>22.6f} "
            f"{binary_ms:>22.6f}"
        )


def main():
    linear_search = registry.get("linear_search")
    binary_search = registry.get("binary_search")

    linear_results = run_experiment(
        algorithm_id=linear_search.id,
        function=linear_search.implementation,
        input_sizes=INPUT_SIZES,
        input_builder=build_search_input,
        runs=RUNS,
    )

    binary_results = run_experiment(
        algorithm_id=binary_search.id,
        function=binary_search.implementation,
        input_sizes=INPUT_SIZES,
        input_builder=build_search_input,
        runs=RUNS,
    )

    all_results = linear_results + binary_results

    save_results(
        results=all_results,
        file_path=OUTPUT_FILE,
    )

    print_results(
        linear_results=linear_results,
        binary_results=binary_results,
    )

    print()
    print(f"Results saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()