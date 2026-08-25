import pytest

from algorithms.implementations.array_access import array_access


def test_array_access_returns_element():
    items = [10, 20, 30, 40]

    assert array_access(items, 2) == 30


def test_array_access_first_element():
    items = [10, 20, 30, 40]

    assert array_access(items, 0) == 10


def test_array_access_last_element():
    items = [10, 20, 30, 40]

    assert array_access(items, 3) == 40


def test_array_access_invalid_index():
    with pytest.raises(IndexError):
        array_access([10, 20, 30], 5)