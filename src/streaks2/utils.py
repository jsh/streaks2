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


def summarize_arr(arr: np.ndarray) -> np.ndarray:
    """
    Replaces the first row with column sums and the first column with row sums.

    Args:
        arr: An mxn ndarray.

    Returns:
        An mxn ndarray with the first row and column replaced.
    """
    m, n = arr.shape
    if m <= 1 or n <= 1:
        return arr.copy()  # Nothing to sum if there's only one row/column or less

    column_sums = np.sum(arr[1:, :], axis=0)
    row_sums = np.sum(arr[:, 1:], axis=1)

    arr_copy = arr.copy()
    arr_copy[0, :] = column_sums
    arr_copy[:, 0] = row_sums

    # Handle the intersection of row 0 and column 0, which should be the sum of all remaining elements.
    arr_copy[0, 0] = np.sum(arr[1:, 1:])

    return arr_copy


def invert_zeros_and_nonzeros(arr: np.ndarray) -> np.ndarray:
    """
    Inverts zeros and non-zeros in an ndarray.

    Args:
        arr: An ndarray of integers.

    Returns:
        An ndarray with 1s where arr contained 0s, and 0s where arr contained non-zeros.
    """
    return np.where(arr == 0, 1, 0)


def create_array_from_kv(keys, vals):
    """
    Creates an ndarray arr where arr[keys[i]] = vals[i] and remaining values are 0.

    Args:
        keys: 1D integer ndarray of keys.
        values: 1D integer ndarray of values (same size as keys).

    Returns:
        1D ndarray arr.
    """

    if keys.size != vals.size:
        raise ValueError("keys and vals arrays must have the same size.")

    if keys.size == 0:
        return np.array([])

    max_index = np.max(keys)
    arr = np.zeros(max_index + 1, dtype=int)  # Initialize arr with zeros

    arr[keys] = vals  # Assign values based on keys and vals

    return arr

    # expected_frequencies[k] = (mean**k * np.exp(-mean)) / math.factorial(k)


# # return expected frequencies for a poisson distribution with mean 1
# def poisson_expected_frequencies(n, mean=1):
#     expected_frequencies = np.zeros(n)
#     for k in range(n):
#         expected_frequencies[k] = (mean**k * np.exp(-mean)) / factorial(k)
#     return expected_frequencies


# # Do the observed frequencies follow a Poisson distribution?
# def poisson_chisquare_test(observed_frequencies, mean=1):
#     n = len(observed_frequencies)
#     expected_frequencies = poisson_expected_frequencies(n, mean)
#     # Scale the expected frequencies to match the total count in A
#     total_count = np.sum(observed_frequencies)
#     expected_frequencies *= total_count
#     # Perform the chi-squared test
#     _, p_value = stats.chisquare(observed_frequencies, f_exp=expected_frequencies)
#     return p_value


# Interpretation:
# alpha = 0.05  # Significance level

# if p_value < alpha:
#     print("Reject the null hypothesis: Observed frequencies are significantly different from expected.")
# else:
#     print("Fail to reject the null hypothesis: Observed frequencies are not significantly different from expected.")
