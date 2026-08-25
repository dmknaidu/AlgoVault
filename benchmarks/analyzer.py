from benchmarks.models import BenchmarkComparison, BenchmarkResult


def compare_results(
    results: list[BenchmarkResult],
    algorithm_a: str,
    algorithm_b: str,
) -> list[BenchmarkComparison]:
    results_a = {
        result.input_size: result
        for result in results
        if result.algorithm_id == algorithm_a
    }

    results_b = {
        result.input_size: result
        for result in results
        if result.algorithm_id == algorithm_b
    }

    common_sizes = sorted(
        set(results_a) & set(results_b)
    )

    comparisons = []

    for input_size in common_sizes:
        result_a = results_a[input_size]
        result_b = results_b[input_size]

        if result_b.median_time == 0:
            speedup = float("inf")
        else:
            speedup = (
                result_a.median_time /
                result_b.median_time
            )

        comparisons.append(
            BenchmarkComparison(
                input_size=input_size,
                algorithm_a=algorithm_a,
                algorithm_b=algorithm_b,
                algorithm_a_time=result_a.median_time,
                algorithm_b_time=result_b.median_time,
                speedup=speedup,
            )
        )

    return comparisons