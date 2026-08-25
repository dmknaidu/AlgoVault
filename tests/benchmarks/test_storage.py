from benchmarks.models import BenchmarkResult
from benchmarks.storage import load_results, save_results


def test_save_and_load_results(tmp_path):
    results = [
        BenchmarkResult(
            algorithm_id="linear_search",
            input_size=1000,
            runs=20,
            min_time=0.001,
            max_time=0.003,
            mean_time=0.002,
            median_time=0.0018,
            environment="local",
        ),
        BenchmarkResult(
            algorithm_id="binary_search",
            input_size=1000,
            runs=20,
            min_time=0.000001,
            max_time=0.000003,
            mean_time=0.000002,
            median_time=0.0000015,
            environment="local",
        ),
    ]

    file_path = tmp_path / "benchmarks.json"

    save_results(results, file_path)

    loaded_results = load_results(file_path)

    assert loaded_results == results


def test_save_results_creates_parent_directory(tmp_path):
    result = BenchmarkResult(
        algorithm_id="test",
        input_size=100,
        runs=5,
        min_time=0.001,
        max_time=0.002,
        mean_time=0.0015,
        median_time=0.0014,
        environment="local",
    )

    file_path = tmp_path / "nested" / "data" / "results.json"

    save_results([result], file_path)

    assert file_path.exists()


def test_saved_file_contains_json_array(tmp_path):
    result = BenchmarkResult(
        algorithm_id="test",
        input_size=100,
        runs=5,
        min_time=0.001,
        max_time=0.002,
        mean_time=0.0015,
        median_time=0.0014,
        environment="local",
    )

    file_path = tmp_path / "results.json"

    save_results([result], file_path)

    loaded_results = load_results(file_path)

    assert len(loaded_results) == 1
    assert loaded_results[0].algorithm_id == "test"