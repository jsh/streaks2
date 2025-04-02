import numpy as np

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


def test_invert_zeros_and_nonzeros():
    arr = np.array([[0, 1, 0], [1, 0, 1]])
    expected = np.array([[1, 0, 1], [0, 1, 0]])
    result = utils.invert_zeros_and_nonzeros(arr)
    np.testing.assert_array_equal(result, expected)

    arr2 = np.array([[0, 0], [0, 0]])
    expected2 = np.array([[1, 1], [1, 1]])
    result2 = utils.invert_zeros_and_nonzeros(arr2)
    np.testing.assert_array_equal(result2, expected2)

    arr3 = np.array([[1, 2], [3, 4]])
    expected3 = np.array([[0, 0], [0, 0]])
    result3 = utils.invert_zeros_and_nonzeros(arr3)
    np.testing.assert_array_equal(result3, expected3)


def test_invert_zeros_and_nonzeros_dtype():
    arr = np.array([[0, 1, 0], [1, 0, 1]])
    result = utils.invert_zeros_and_nonzeros(arr)
    assert result.dtype == int
