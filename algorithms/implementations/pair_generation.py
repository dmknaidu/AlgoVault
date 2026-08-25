def generate_pairs(items: list) -> list[tuple]:
    pairs = []

    for first in items:
        for second in items:
            pairs.append((first, second))

    return pairs