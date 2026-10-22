import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "searching"))

from linear_search import linear_search, linear_search_all


def test_finds_element():
    assert linear_search([5, 3, 8, 1], 8) == 2


def test_first_and_last_positions():
    assert linear_search([5, 3, 8, 1], 5) == 0
    assert linear_search([5, 3, 8, 1], 1) == 3


def test_missing_element():
    assert linear_search([5, 3, 8, 1], 42) == -1


def test_empty_list():
    assert linear_search([], 1) == -1


def test_returns_first_occurrence():
    assert linear_search([2, 7, 2, 7], 7) == 1


def test_works_with_strings():
    assert linear_search(["a", "b", "c"], "c") == 2
    assert linear_search("hello", "l") == 2


def test_find_all():
    assert linear_search_all([3, 1, 3, 2, 3], 3) == [0, 2, 4]
    assert linear_search_all([], 3) == []
