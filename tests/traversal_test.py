"""
test_array_traversal.py

Test suite for array traversal algorithms:
- Linear Search
- Binary Search

Covers:
- Element present
- Element absent
- Edge cases (empty array, single element)
- Duplicates
- Boundaries (first / last element)
- Binary-search-specific constraints

How to run:
    pip install pytest
    pytest -q
"""

import pytest
import importlib

# Import the user's implementation
from Algorithms import serach_algorithms as algos


# -------------------------
# Helpers
# -------------------------

def normalize_result(result):
    """
    Normalize search results.

    Acceptable 'not found' values:
    - None
    - -1
    """
    if result is None:
        return -1
    return result


def assert_found(arr, target, index):
    """Assert that the returned index is valid and correct."""
    assert index != -1, f"Expected to find {target}, but search returned not found."
    assert 0 <= index < len(arr), "Returned index is out of bounds."
    assert arr[index] == target, "Returned index does not point to target value."


def assert_not_found(index):
    """Assert that the target was correctly not found."""
    assert index == -1, "Expected target to be absent, but search returned an index."


# -------------------------
# LINEAR SEARCH TESTS
# -------------------------

def test_linear_found_middle():
    """Target exists in the middle of the array."""
    arr = [3, 1, 4, 6, 9]
    target = 4
    idx = normalize_result(algos.linear_search(arr, target))
    assert_found(arr, target, idx)


def test_linear_found_first():
    """Target exists at index 0."""
    arr = [7, 2, 5, 1]
    target = 7
    idx = normalize_result(algos.linear_search(arr, target))
    assert_found(arr, target, idx)


def test_linear_found_last():
    """Target exists at the last index."""
    arr = [2, 4, 6, 8]
    target = 8
    idx = normalize_result(algos.linear_search(arr, target))
    assert_found(arr, target, idx)


def test_linear_not_found():
    """Target does not exist in array."""
    arr = [1, 3, 5, 7]
    target = 4
    idx = normalize_result(algos.linear_search(arr, target))
    assert_not_found(idx)


def test_linear_empty_array():
    """Edge case: empty array."""
    arr = []
    target = 10
    idx = normalize_result(algos.linear_search(arr, target))
    assert_not_found(idx)


def test_linear_single_element_found():
    """Single-element array where target exists."""
    arr = [42]
    target = 42
    idx = normalize_result(algos.linear_search(arr, target))
    assert_found(arr, target, idx)


def test_linear_single_element_not_found():
    """Single-element array where target does not exist."""
    arr = [42]
    target = 7
    idx = normalize_result(algos.linear_search(arr, target))
    assert_not_found(idx)


def test_linear_duplicates():
    """
    Array contains duplicate values.
    Linear search may return ANY valid matching index.
    """
    arr = [5, 1, 5, 3, 5]
    target = 5
    idx = normalize_result(algos.linear_search(arr, target))
    assert_found(arr, target, idx)


# -------------------------
# BINARY SEARCH TESTS
# -------------------------

def test_binary_found_middle():
    """Target exists in the middle of sorted array."""
    arr = [1, 3, 5, 7, 9]
    target = 5
    idx = normalize_result(algos.binary_search(arr, target))
    assert_found(arr, target, idx)


def test_binary_found_first():
    """Target exists at index 0."""
    arr = [2, 4, 6, 8]
    target = 2
    idx = normalize_result(algos.binary_search(arr, target))
    assert_found(arr, target, idx)


def test_binary_found_last():
    """Target exists at last index."""
    arr = [2, 4, 6, 8]
    target = 8
    idx = normalize_result(algos.binary_search(arr, target))
    assert_found(arr, target, idx)


def test_binary_not_found():
    """Target does not exist in sorted array."""
    arr = [1, 3, 5, 7]
    target = 6
    idx = normalize_result(algos.binary_search(arr, target))
    assert_not_found(idx)


def test_binary_empty_array():
    """Edge case: empty array."""
    arr = []
    target = 3
    idx = normalize_result(algos.binary_search(arr, target))
    assert_not_found(idx)


def test_binary_single_element_found():
    """Single-element array where target exists."""
    arr = [10]
    target = 10
    idx = normalize_result(algos.binary_search(arr, target))
    assert_found(arr, target, idx)


def test_binary_single_element_not_found():
    """Single-element array where target does not exist."""
    arr = [10]
    target = 5
    idx = normalize_result(algos.binary_search(arr, target))
    assert_not_found(idx)


def test_binary_duplicates():
    """
    Sorted array with duplicates.
    Binary search may return ANY valid matching index.
    """
    arr = [1, 2, 2, 2, 3]
    target = 2
    idx = normalize_result(algos.binary_search(arr, target))
    assert_found(arr, target, idx)


def test_binary_unsorted_input():
    """
    IMPORTANT CONCEPT TEST:
    Binary search assumes sorted input.

    This test documents the assumption.
    We do NOT enforce correctness here, but this test exists
    to remind you that unsorted input = undefined behavior.
    """
    arr = [3, 1, 4, 2]
    target = 4

    idx = normalize_result(algos.binary_search(arr, target))

    # Either behavior is acceptable:
    # - returns not found
    # - returns incorrect index
    # This test exists purely for documentation / learning.
    assert True
