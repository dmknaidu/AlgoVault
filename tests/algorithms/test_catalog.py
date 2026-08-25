from algorithms.catalog import registry


def test_catalog_contains_linear_search():
    algorithm = registry.get("linear_search")

    assert algorithm.name == "Linear Search"
    assert algorithm.time_complexity == "O(n)"


def test_catalog_contains_binary_search():
    algorithm = registry.get("binary_search")

    assert algorithm.name == "Binary Search"
    assert algorithm.time_complexity == "O(log n)"


def test_catalog_contains_array_access():
    algorithm = registry.get("array_access")

    assert algorithm.name == "Array Access"
    assert algorithm.time_complexity == "O(1)"


def test_catalog_contains_pair_generation():
    algorithm = registry.get("pair_generation")

    assert algorithm.name == "Pair Generation"
    assert algorithm.time_complexity == "O(n²)"


def test_searching_algorithms():
    algorithms = registry.list_by_category("Searching")

    ids = {algorithm.id for algorithm in algorithms}

    assert ids == {"linear_search", "binary_search"}