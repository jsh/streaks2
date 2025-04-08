import numpy as np
import pytest

from streaks2 import utils


def test_random_permutation():
    n = 5
    permutation = utils.random_permutation(n)
    assert len(permutation) == n
    assert all(i in permutation for i in range(n))


def test_add_summary_row_column():
    arr = np.array([[0, 0, 0], [0, 1, 2], [0, 3, 4]])
    expected = np.array([[10, 4, 6], [3, 1, 2], [7, 3, 4]])
    result = utils.add_summary_row_column(
        arr.copy()
    )  # copy to avoid modifying original
    np.testing.assert_array_equal(result, expected)

    arr2 = np.array([[0, 0], [0, 0]])
    expected2 = np.array([[0, 0], [0, 0]])
    result2 = utils.add_summary_row_column(arr2.copy())
    np.testing.assert_array_equal(result2, expected2)

    arr3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    expected3 = np.array([[28, 13, 15], [11, 5, 6], [17, 8, 9]])
    result3 = utils.add_summary_row_column(arr3.copy())
    np.testing.assert_array_equal(result3, np.array(expected3))

    arr4 = np.array([[1]])
    expected4 = np.array([[1]])
    result4 = utils.add_summary_row_column(arr4.copy())
    np.testing.assert_array_equal(result4, expected4)

    arr5 = np.array([[1, 2], [3, 4]])
    expected5 = np.array([[4, 4], [4, 4]])
    result5 = utils.add_summary_row_column(arr5.copy())
    np.testing.assert_array_equal(result5, expected5)
    arr6 = np.array([[1, 2, 3]])
    expected6 = np.array([[1, 2, 3]])
    result6 = utils.add_summary_row_column(arr6.copy())
    np.testing.assert_array_equal(result6, expected6)

    arr7 = np.array([[1], [2], [3]])
    expected7 = np.array([[1], [2], [3]])
    result7 = utils.add_summary_row_column(arr7.copy())
    np.testing.assert_array_equal(result7, expected7)


def test_add_summary_row_column_value_error():
    arr = np.array([1, 2, 3])
    with pytest.raises(ValueError, match=r"^Input array must be 2-dimensional.$"):
        utils.add_summary_row_column(arr)


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


def test_invert_zeros_and_nonzeros_value_error():
    arr = np.array(["a", "b", "c"])
    with pytest.raises(ValueError, match=r"^Input array must be of a numeric type.$"):
        utils.invert_zeros_and_nonzeros(arr)


def test_invert_zeros_and_nonzeros_dtype():
    arr = np.array([[0, 1, 0], [1, 0, 1]])
    result = utils.invert_zeros_and_nonzeros(arr)
    assert result.dtype == int


def test_create_array_from_kv():
    keys = np.array([0, 1, 2])
    vals = np.array([10, 20, 30])
    expected = np.array([10, 20, 30])
    result = utils.create_array_from_kv(keys, vals)
    np.testing.assert_array_equal(result, expected)

    keys2 = np.array([2, 0, 1])
    vals2 = np.array([30, 10, 20])
    expected2 = np.array([10, 20, 30])
    result2 = utils.create_array_from_kv(keys2, vals2)
    np.testing.assert_array_equal(result2, expected2)

    keys3 = np.array([])
    vals3 = np.array([])
    expected3 = np.array([])
    result3 = utils.create_array_from_kv(keys3, vals3)
    np.testing.assert_array_equal(result3, expected3)

    keys4 = np.array([5, 2, 0])
    vals4 = np.array([50, 20, 0])
    expected4 = np.array([0, 0, 20, 0, 0, 50])
    result4 = utils.create_array_from_kv(keys4, vals4)
    np.testing.assert_array_equal(result4, expected4)

    keys5 = np.array([0])
    vals5 = np.array([100])
    expected5 = np.array([100])
    result5 = utils.create_array_from_kv(keys5, vals5)
    np.testing.assert_array_equal(result5, expected5)

    keys6 = np.array([1, 3, 5])
    vals6 = np.array([10, 30, 50])
    expected6 = np.array([0, 10, 0, 30, 0, 50])
    result6 = utils.create_array_from_kv(keys6, vals6)
    np.testing.assert_array_equal(result6, expected6)
    assert result6.dtype == int


def test_create_array_from_kv_raises():
    keys = np.array([0, 1, 2])
    vals = np.array([10, 20])
    with pytest.raises(
        ValueError, match=r"^keys and vals arrays must have the same size.$"
    ):
        utils.create_array_from_kv(keys, vals)

    keys_multi = np.array([[0, 1], [2, 3]])
    vals_multi = np.array([[10, 20], [30, 40]])
    with pytest.raises(
        ValueError, match=r"^keys and vals arrays must be 1-dimensional.$"
    ):
        utils.create_array_from_kv(keys_multi, vals_multi)

    keys_multi2 = np.array([0, 1, 2])
    vals_multi2 = np.array([[10, 20, 30]])
    with pytest.raises(
        ValueError, match=r"^keys and vals arrays must be 1-dimensional.$"
    ):
        utils.create_array_from_kv(keys_multi2, vals_multi2)
