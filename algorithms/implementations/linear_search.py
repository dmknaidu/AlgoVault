from typing import Any


def linear_search(items: list[Any], target: Any) -> int:
    for index, value in enumerate(items):
        if value == target:
            return index

    return -1