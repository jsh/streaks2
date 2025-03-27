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


def test_binary_array_dtype():
    arr = np.array([[0, 1, 2], [3, 0, 4]])
    result = utils.create_binary_arr(arr)
    assert result.dtype == int


def test_complement_binary_arr():
    arr = np.array([[0, 1, 0], [1, 0, 1]])
    expected = np.array([[0, 0, 0], [0, 1, 0]])
    result = utils.complement_binary_arr(arr)
    np.testing.assert_array_equal(result, expected)

    arr2 = np.array([[0, 0], [0, 0]])
    expected2 = np.array([[0, 0], [0, 1]])
    result2 = utils.complement_binary_arr(arr2)
    np.testing.assert_array_equal(result2, expected2)


def test_complement_array_dtype():
    arr = np.array([[0, 1, 0], [1, 0, 1]])
    result = utils.complement_binary_arr(arr)
    assert result.dtype == int


# def test_approx_equal():
#     arr1 = np.array([1.0, 2.0, 3.0])
#     arr2 = np.array([1.000001, 2.000002, 3.000003])
#     utils.assert_array_approx_equal(arr1, arr2)  # Should pass

#     arr3 = np.array([1.0, 2.0, 3.0])
#     arr4 = np.array([1.001, 2.002, 3.003])
#     try:
#         utils.assert_array_approx_equal(arr3, arr4)  # Should raise AssertionError
#         # assert False, "Arrays are not approximately equal"
#     except AssertionError:
#         pass

#     arr5 = np.array([1.0, 2.0, 3.0])
#     arr6 = np.array([1.000001, 2.000002, 3.000003, 4.0])
#     try:
#         utils.assert_array_approx_equal(arr5, arr6)
#         assert False, "Expected AssertionError"
#     except AssertionError:
#         pass

#     arr7 = np.array([1.0, 2.0, 3.0])
#     arr8 = np.array([1.000001, 2.000002, 3.000003])
#     utils.assert_array_approx_equal(arr7, arr8, tolerance=1e-5)

#     arr9 = np.array([1.0, 2.0, 3.0])
#     arr10 = np.array([1.000001, 2.000002, 3.000003])
#     utils.assert_array_approx_equal(arr9, arr10, tolerance=1e-7)

#     arr11 = np.array([1.0, 2.0, 3.0])
#     arr12 = np.array([1.000001, 2.000002, 3.000003])
#     try:
#         utils.assert_array_approx_equal(arr11, arr12, tolerance=1e-8)
#         assert False, "Expected AssertionError"
#     except AssertionError:
#         pass
