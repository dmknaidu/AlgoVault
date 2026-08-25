from benchmarks.experiments import run_experiment


def test_run_experiment_runs_all_input_sizes():
    def constant_function(items):
        return items[0]

    def build_input(size):
        return ([0] * size,)

    results = run_experiment(
        algorithm_id="test_constant",
        function=constant_function,
        input_sizes=[10, 100, 1000],
        input_builder=build_input,
        runs=3,
    )

    assert len(results) == 3

    assert [result.input_size for result in results] == [
        10,
        100,
        1000,
    ]

    assert all(result.algorithm_id == "test_constant" for result in results)
    assert all(result.runs == 3 for result in results)


def test_run_experiment_uses_input_builder():
    received_sizes = []

    def test_function(items):
        return items[0]

    def build_input(size):
        received_sizes.append(size)
        return ([size],)

    run_experiment(
        algorithm_id="test",
        function=test_function,
        input_sizes=[10, 20, 30],
        input_builder=build_input,
        runs=1,
    )

    assert received_sizes == [10, 20, 30]


def test_run_experiment_with_empty_input_sizes():
    def test_function(items):
        return items

    def build_input(size):
        return ([0] * size,)

    results = run_experiment(
        algorithm_id="test",
        function=test_function,
        input_sizes=[],
        input_builder=build_input,
        runs=1,
    )

    assert results == []