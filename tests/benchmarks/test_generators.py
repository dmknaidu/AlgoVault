from benchmarks.generators import (
    generate_random_array,
    generate_reverse_sorted_array,
    generate_sorted_array,
)


def test_random_array_has_requested_size():
    result = generate_random_array(10, seed=42)

    assert len(result) == 10


def test_random_array_is_reproducible():
    first = generate_random_array(10, seed=42)
    second = generate_random_array(10, seed=42)

    assert first == second


def test_different_seeds_produce_different_data():
    first = generate_random_array(10, seed=42)
    second = generate_random_array(10, seed=100)

    assert first != second


def test_random_array_empty():
    assert generate_random_array(0, seed=42) == []


def test_random_array_rejects_negative_size():
    import pytest

    with pytest.raises(ValueError):
        generate_random_array(-1, seed=42)


def test_sorted_array():
    assert generate_sorted_array(5) == [0, 1, 2, 3, 4]


def test_reverse_sorted_array():
    assert generate_reverse_sorted_array(5) == [4, 3, 2, 1, 0]


def test_sorted_array_empty():
    assert generate_sorted_array(0) == []


def test_reverse_sorted_array_empty():
    assert generate_reverse_sorted_array(0) == []