from algorithms.implementations.pair_generation import generate_pairs


def test_generate_pairs():
    items = [1, 2, 3]

    result = generate_pairs(items)

    assert len(result) == 9
    assert (1, 1) in result
    assert (1, 3) in result
    assert (3, 1) in result
    assert (3, 3) in result


def test_generate_pairs_empty_list():
    assert generate_pairs([]) == []


def test_generate_pairs_single_element():
    assert generate_pairs([10]) == [(10, 10)]