import os
import random
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "searching"))

from binary_search import binary_search, binary_search_recursive, lower_bound

SEARCHES = [binary_search, binary_search_recursive]


def test_finds_every_element():
    data = [1, 3, 5, 7, 9, 11, 13]
    for search in SEARCHES:
        for index, value in enumerate(data):
            assert search(data, value) == index


def test_missing_elements():
    data = [1, 3, 5, 7]
    for search in SEARCHES:
        for target in (0, 2, 4, 6, 8):
            assert search(data, target) == -1


def test_empty_and_single():
    for search in SEARCHES:
        assert search([], 5) == -1
        assert search([5], 5) == 0
        assert search([5], 4) == -1


def test_strings():
    words = ["apple", "banana", "cherry", "date"]
    for search in SEARCHES:
        assert search(words, "cherry") == 2
        assert search(words, "fig") == -1


def test_matches_python_index_on_random_data():
    rng = random.Random(42)
    for _ in range(200):
        data = sorted(rng.sample(range(1000), rng.randint(0, 50)))
        target = rng.randint(0, 999)
        expected = data.index(target) if target in data else -1
        for search in SEARCHES:
            assert search(data, target) == expected


def test_lower_bound():
    assert lower_bound([1, 2, 2, 2, 5], 2) == 1
    assert lower_bound([1, 2, 2, 2, 5], 0) == 0
    assert lower_bound([1, 2, 2, 2, 5], 3) == 4
    assert lower_bound([1, 2, 2, 2, 5], 6) == 5
    assert lower_bound([], 1) == 0
