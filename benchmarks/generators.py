import random


def generate_random_array(
    size: int,
    seed: int | None = None,
) -> list[int]:
    if size < 0:
        raise ValueError("size must be non-negative")

    rng = random.Random(seed)

    return [rng.randint(0, size * 10) for _ in range(size)]


def generate_sorted_array(
    size: int,
) -> list[int]:
    if size < 0:
        raise ValueError("size must be non-negative")

    return list(range(size))


def generate_reverse_sorted_array(
    size: int,
) -> list[int]:
    if size < 0:
        raise ValueError("size must be non-negative")

    return list(range(size - 1, -1, -1))