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


def assert_array_approx_equal(arr1, arr2, tolerance=1e-6):
    """
    Asserts that two NumPy arrays of floats are approximately equal element-wise.

    Args:
        arr1: The first NumPy array.
        arr2: The second NumPy array.
        tolerance: The maximum absolute difference allowed between corresponding elements.
                   Defaults to 1e-6.

    Raises:
        AssertionError: If the arrays are not approximately equal.
    """
    assert arr1.shape == arr2.shape, (
        f"Arrays have different shapes: {arr1.shape} vs {arr2.shape}"
    )

    diff = np.abs(arr1 - arr2)

    assert np.all(diff <= tolerance), (
        f"Arrays are not approximately equal within tolerance {tolerance}. Max difference: {np.max(diff)}"
    )


def create_array_from_kv(K, V):
    """
    Creates an ndarray A where A[K[i]] = V[i] and remaining values are 0.

    Args:
        K: 1D integer ndarray of keys.
        V: 1D integer ndarray of values (same size as K).

    Returns:
        1D ndarray A.
    """

    if K.size != V.size:
        raise ValueError("K and V arrays must have the same size.")

    if K.size == 0:
        return np.array([])

    max_index = np.max(K)
    A = np.zeros(max_index + 1, dtype=V.dtype)  # Initialize A with zeros

    A[K] = V  # Assign values based on K and V

    return A
