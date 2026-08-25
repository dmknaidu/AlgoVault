from pathlib import Path

from benchmarks.analyzer import compare_results
from benchmarks.storage import load_results


INPUT_FILE = Path("data/benchmarks/search_experiment.json")


def main():
    results = load_results(INPUT_FILE)

    comparisons = compare_results(
        results=results,
        algorithm_a="linear_search",
        algorithm_b="binary_search",
    )

    print("Search Performance Analysis")
    print("=" * 80)
    print(
        f"{'Input Size':>12} "
        f"{'Linear (ms)':>18} "
        f"{'Binary (ms)':>18} "
        f"{'Speedup':>15}"
    )
    print("-" * 80)

    for comparison in comparisons:
        linear_ms = comparison.algorithm_a_time * 1000
        binary_ms = comparison.algorithm_b_time * 1000

        print(
            f"{comparison.input_size:>12} "
            f"{linear_ms:>18.6f} "
            f"{binary_ms:>18.6f} "
            f"{comparison.speedup:>14.2f}x"
        )


if __name__ == "__main__":
    main()