from typing import Any


def binary_search(items: list[Any], target: Any) -> int:
    left = 0
    right = len(items) - 1

    while left <= right:
        middle = (left + right) // 2

        if items[middle] == target:
            return middle

        if items[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1