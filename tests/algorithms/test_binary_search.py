from algorithms.implementations.binary_search import binary_search


def test_binary_search_finds_middle_element():
    items = [10, 20, 30, 40, 50]
    assert binary_search(items, 30) == 2


def test_binary_search_finds_first_element():
    items = [10, 20, 30, 40, 50]
    assert binary_search(items, 10) == 0


def test_binary_search_finds_last_element():
    items = [10, 20, 30, 40, 50]
    assert binary_search(items, 50) == 4


def test_binary_search_returns_minus_one_when_missing():
    items = [10, 20, 30, 40, 50]
    assert binary_search(items, 35) == -1


def test_binary_search_empty_list():
    assert binary_search([], 10) == -1


def test_binary_search_single_element_found():
    assert binary_search([10], 10) == 0


def test_binary_search_single_element_missing():
    assert binary_search([10], 20) == -1


def test_binary_search_target_smaller_than_all_elements():
    items = [10, 20, 30, 40, 50]
    assert binary_search(items, 5) == -1


def test_binary_search_target_greater_than_all_elements():
    items = [10, 20, 30, 40, 50]
    assert binary_search(items, 60) == -1