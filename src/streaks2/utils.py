import numpy as np
import sympy

GAMMA = float(sympy.S.EulerGamma)
SUMS = 0
COL_AXIS, ROW_AXIS = 0, 1


# generate a random permutation of range(n)
def random_permutation(n):
    """
    Generate a random permutation of integers from 0 to n-1.

    Args:
        n (int): The upper limit (exclusive) for the range of integers to permute.

    Returns:
        list: A list containing a random permutation of integers from 0 to n-1.
    """
    return np.random.permutation(n)


def summarize_arr(arr):
    assert np.all(arr[SUMS] == 0), "First row is not all zeros."
    assert np.all(arr[:, SUMS] == 0), "First column is not all zeros."
    col_sums = np.sum(arr, axis=COL_AXIS)  # Sum along columns
    row_sums = np.sum(arr, axis=ROW_AXIS)  # Sum along rows
    total = sum(col_sums)
    assert total == sum(row_sums.flatten())  # cross-check
    arr[SUMS] = col_sums
    arr[:, SUMS] = row_sums.flatten()
    arr[SUMS, SUMS] = total
    return arr


def create_binary_arr(arr):
    """
    Creates a binary array with 1s where arr is non-zero, and 0s otherwise.

    Args:
      arr: The input NumPy ndarray.

    Returns:
      A NumPy ndarray of the same shape, with 1s and 0s.
    """
    return (arr != 0).astype(int)


def complement_binary_arr(arr):
    """
    Creates a binary array with 0s where arr is non-zero, and 1s otherwise.

    Args:
      arr: The input NumPy ndarray.

    Returns:
      A NumPy ndarray of the same shape, with 1s and 0s.
    """
    complement = (arr == 0).astype(int)
    complement[SUMS] = 0
    complement[:, SUMS] = 0
    return complement
