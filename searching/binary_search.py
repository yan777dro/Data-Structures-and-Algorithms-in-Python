"""Binary search.

Find a target in a SORTED sequence by repeatedly halving the search range.
Each step compares the target with the middle element and throws away the
half that cannot contain it.

Time complexity:
    Best    O(1)      - target is the first middle element checked
    Average O(log n)
    Worst   O(log n)
Space complexity:
    Iterative O(1)
    Recursive O(log n) - one stack frame per halving

The input must be sorted in ascending order, otherwise results are wrong.
"""

from typing import Any, Sequence


def binary_search(items: Sequence[Any], target: Any) -> int:
    """Return the index of target in sorted items, or -1 if absent.

    >>> binary_search([1, 3, 5, 7, 9, 11], 7)
    3
    >>> binary_search([1, 3, 5, 7, 9, 11], 4)
    -1
    >>> binary_search([], 1)
    -1
    """
    low, high = 0, len(items) - 1

    while low <= high:
        mid = (low + high) // 2  # middle of the current range
        if items[mid] == target:
            return mid
        if items[mid] < target:
            low = mid + 1   # target can only be in the right half
        else:
            high = mid - 1  # target can only be in the left half

    return -1  # range is empty, so target is not present


def binary_search_recursive(items: Sequence[Any], target: Any,
                            low: int = 0, high: int | None = None) -> int:
    """Recursive version of binary_search, same result.

    >>> binary_search_recursive([2, 4, 6, 8], 8)
    3
    >>> binary_search_recursive([2, 4, 6, 8], 5)
    -1
    """
    if high is None:
        high = len(items) - 1
    if low > high:
        return -1

    mid = (low + high) // 2
    if items[mid] == target:
        return mid
    if items[mid] < target:
        return binary_search_recursive(items, target, mid + 1, high)
    return binary_search_recursive(items, target, low, mid - 1)


def lower_bound(items: Sequence[Any], target: Any) -> int:
    """Return the first index where target could be inserted to keep order.

    Useful with duplicates: it finds the FIRST occurrence of target.

    >>> lower_bound([1, 2, 2, 2, 5], 2)
    1
    >>> lower_bound([1, 2, 2, 2, 5], 3)
    4
    >>> lower_bound([1, 2, 5], 9)
    3
    """
    low, high = 0, len(items)
    while low < high:
        mid = (low + high) // 2
        if items[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low


if __name__ == "__main__":
    data = [3, 9, 10, 27, 38, 43, 82]
    for target in (43, 3, 50):
        print(f"binary_search({data}, {target}) -> {binary_search(data, target)}")
