from enum import Enum

import numpy as np
import sympy

GAMMA = float(sympy.S.EulerGamma)


class SummaryIndex(Enum):
    SUM = 0  # Index for summary row and column


# def summarize_arr(arr):
#     assert np.all(arr[SUMS] == 0), "First row is not all zeros."
#     assert np.all(arr[:, SUMS] == 0), "First column is not all zeros."
#     col_sums = np.sum(arr, axis=COL_AXIS)  # Sum along columns
#     row_sums = np.sum(arr, axis=ROW_AXIS)  # Sum along rows
#     total = sum(col_sums)
#     assert total == sum(row_sums.flatten())  # cross-check
#     arr[SUMS] = col_sums
#     arr[:, SUMS] = row_sums.flatten()
#     arr[SUMS, SUMS] = total
#     return arr


def add_summary_row_column(arr: np.ndarray) -> np.ndarray:
    """Adds a summary row and column to a 2D NumPy array.

    The first row is replaced with column sums, and the first column is replaced with row sums.
    The element at [0, 0] is the sum of all elements in the original array (excluding the summary row and column).

    Args:
        arr: A 2D NumPy array.

    Returns:
        A new NumPy array with the summary row and column added.
    """
    if arr.ndim != 2:
        raise ValueError("Input array must be 2-dimensional.")

    m, n = arr.shape
    if m <= 1 or n <= 1:
        return arr.copy()  # Nothing to sum if there's only one row/column or less

    column_sums = np.sum(arr[1:, :], axis=0)
    row_sums = np.sum(arr[:, 1:], axis=1)

    result = np.zeros_like(arr)  # Create a new array
    result[0, :] = column_sums
    result[:, 0] = row_sums

    # Handle the intersection of row 0 and column 0, which should be the sum of all remaining elements.
    result[0, 0] = np.sum(arr[1:, 1:])

    return result


def invert_zeros_and_nonzeros(arr: np.ndarray) -> np.ndarray:
    """Inverts zeros and non-zeros in a NumPy array.

    Args:
        arr: A NumPy array of integers.

    Returns:
        A NumPy array with 1s where arr contained 0s, and 0s where arr contained non-zeros.
    """
    if not np.issubdtype(arr.dtype, np.number):
        raise ValueError("Input array must be of a numeric type.")
    return np.where(arr == 0, 1, 0)


def create_array_from_kv(keys: np.ndarray, vals: np.ndarray) -> np.ndarray:
    """Creates a NumPy array where arr[keys[i]] = vals[i] and remaining values are 0.

    Args:
        keys: 1D integer NumPy array of keys.
        vals: 1D integer NumPy array of values (same size as keys).

    Returns:
        A 1D NumPy array arr.
    """
    if keys.ndim != 1 or vals.ndim != 1:
        raise ValueError("keys and vals arrays must be 1-dimensional.")

    if keys.size != vals.size:
        raise ValueError("keys and vals arrays must have the same size.")

    if keys.size == 0:
        return np.array([])

    max_index = np.max(keys)
    arr = np.zeros(max_index + 1, dtype=int)  # Initialize arr with zeros

    arr[keys] = vals  # Assign values based on keys and vals

    return arr


def random_permutation(n):
    """
        Generate a random permutation of integers from 0 to n-1.

        Args:
            n (int): The upper limit (exclusive) for the range of integers
     to permute.

        Returns:
            list: A list containing a random permutation of integers from
    0 to n-1.
    """
    return np.random.permutation(n)
