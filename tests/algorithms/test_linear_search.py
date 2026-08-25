from algorithms.implementations.linear_search import linear_search


def test_linear_search_finds_target():
    assert linear_search([10, 20, 30, 40], 30) == 2


def test_linear_search_returns_minus_one_when_missing():
    assert linear_search([10, 20, 30, 40], 99) == -1


def test_linear_search_finds_first_occurrence():
    assert linear_search([10, 20, 20, 30], 20) == 1


def test_linear_search_empty_list():
    assert linear_search([], 10) == -1