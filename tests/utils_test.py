import numpy as np
import pytest

from streaks2 import utils


def test_random_permutation():
    n = 5
    permutation = utils.random_permutation(n)
    assert len(permutation) == n
    assert all(i in permutation for i in range(n))


def test_summarize_arr():
    arr = np.array([[0, 0, 0], [0, 1, 2], [0, 3, 4]])
    expected = np.array([[10, 4, 6], [3, 1, 2], [7, 3, 4]])
    result = utils.summarize_arr(arr.copy())  # copy to avoid modifying original
    np.testing.assert_array_equal(result, expected)

    arr2 = np.array([[0, 0], [0, 0]])
    expected2 = np.array([[0, 0], [0, 0]])
    result2 = utils.summarize_arr(arr2.copy())
    np.testing.assert_array_equal(result2, expected2)


def test_summarize_arr_assertions():
    arr = np.array([[0, 0, 0], [1, 1, 2], [0, 3, 4]])
    with pytest.raises(AssertionError, match=r"^First column is not all zeros.$"):
        utils.summarize_arr(arr)

    arr = np.array([[0, 1, 0], [0, 1, 2], [0, 3, 4]])
    with pytest.raises(AssertionError, match=r"^First row is not all zeros.$"):
        utils.summarize_arr(arr)


def test_create_binary_arr():
    arr = np.array([[0, 1, 2], [3, 0, 4]])
    expected = np.array([[0, 1, 1], [1, 0, 1]])
    result = utils.create_binary_arr(arr)
    np.testing.assert_array_equal(result, expected)

    arr2 = np.array([[0, 0], [0, 0]])
    expected2 = np.array([[0, 0], [0, 0]])
    result2 = utils.create_binary_arr(arr2)
    np.testing.assert_array_equal(result2, expected2)


def test_complement_binary_arr():
    arr = np.array([[0, 1, 0], [1, 0, 1]])
    expected = np.array([[0, 0, 0], [0, 1, 0]])
    result = utils.complement_binary_arr(arr)
    np.testing.assert_array_equal(result, expected)

    arr2 = np.array([[0, 0], [0, 0]])
    expected2 = np.array([[0, 0], [0, 1]])
    result2 = utils.complement_binary_arr(arr2)
    np.testing.assert_array_equal(result2, expected2)
