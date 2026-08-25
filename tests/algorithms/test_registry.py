import pytest

from algorithms.models import Algorithm
from algorithms.registry import AlgorithmRegistry


def dummy_algorithm():
    return "ok"


def test_register_and_get_algorithm():
    registry = AlgorithmRegistry()

    algorithm = Algorithm(
        id="dummy",
        name="Dummy",
        category="Testing",
        description="Test algorithm.",
        time_complexity="O(1)",
        space_complexity="O(1)",
        implementation=dummy_algorithm,
    )

    registry.register(algorithm)

    result = registry.get("dummy")

    assert result.name == "Dummy"
    assert result.time_complexity == "O(1)"


def test_duplicate_algorithm_is_rejected():
    registry = AlgorithmRegistry()

    algorithm = Algorithm(
        id="dummy",
        name="Dummy",
        category="Testing",
        description="Test algorithm.",
        time_complexity="O(1)",
        space_complexity="O(1)",
        implementation=dummy_algorithm,
    )

    registry.register(algorithm)

    with pytest.raises(ValueError):
        registry.register(algorithm)


def test_missing_algorithm_is_rejected():
    registry = AlgorithmRegistry()

    with pytest.raises(KeyError):
        registry.get("does_not_exist")