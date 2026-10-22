"""Linear search.

Scan a sequence from left to right until the target is found.

Time complexity:
    Best    O(1)   - target is the first element
    Average O(n)
    Worst   O(n)   - target is last or not present
Space complexity: O(1)

Works on unsorted data, unlike binary search.
"""

from typing import Any, Sequence


def linear_search(items: Sequence[Any], target: Any) -> int:
    """Return the index of the first occurrence of target, or -1 if absent.

    >>> linear_search([4, 2, 7, 1], 7)
    2
    >>> linear_search([4, 2, 7, 1], 9)
    -1
    >>> linear_search([], 1)
    -1
    """
    for index, value in enumerate(items):
        if value == target:
            return index
    return -1


def linear_search_all(items: Sequence[Any], target: Any) -> list[int]:
    """Return the indices of every occurrence of target.

    >>> linear_search_all([3, 1, 3, 2, 3], 3)
    [0, 2, 4]
    >>> linear_search_all([1, 2], 5)
    []
    """
    return [index for index, value in enumerate(items) if value == target]


if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    for target in (43, 10, 99):
        print(f"linear_search({data}, {target}) -> {linear_search(data, target)}")
