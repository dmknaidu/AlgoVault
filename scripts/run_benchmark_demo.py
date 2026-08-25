from algorithms.catalog import registry
from benchmarks.generators import generate_sorted_array
from benchmarks.runner import run_benchmark


def main():
    input_size = 10_000
    runs = 20

    items = generate_sorted_array(input_size)
    target = items[-1]

    linear_search = registry.get("linear_search")
    binary_search = registry.get("binary_search")

    linear_result = run_benchmark(
        algorithm_id=linear_search.id,
        function=linear_search.implementation,
        args=(items, target),
        input_size=input_size,
        runs=runs,
    )

    binary_result = run_benchmark(
        algorithm_id=binary_search.id,
        function=binary_search.implementation,
        args=(items, target),
        input_size=input_size,
        runs=runs,
    )

    print("Benchmark Comparison")
    print("=" * 60)

    for result in (linear_result, binary_result):
        print(f"\nAlgorithm: {result.algorithm_id}")
        print(f"Input size: {result.input_size}")
        print(f"Runs: {result.runs}")
        print(f"Minimum: {result.min_time:.9f} sec")
        print(f"Maximum: {result.max_time:.9f} sec")
        print(f"Mean: {result.mean_time:.9f} sec")
        print(f"Median: {result.median_time:.9f} sec")


if __name__ == "__main__":
    main()