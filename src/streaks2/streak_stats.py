import math
from collections import Counter

import numpy as np

from streaks2.streaks import KvStreaks
from streaks2.utils import random_permutation

SUMS = 0
COL_AXIS, ROW_AXIS = 0, 1


def print_kv_streaks(n):
    for kv_streaks in KvStreaks.generate_kv_streaks_for_all_permutations(n):
        print(kv_streaks)


def count_streak_lengths(n):
    streak_length_counts = Counter()
    for kv_streaks in KvStreaks.generate_kv_streaks_for_all_permutations(n):
        streak_length_counts[len(kv_streaks)] += 1
    return dict(sorted(streak_length_counts.items()))


def mean_streaks(n, trials=1):
    kv_streaks_count = []
    for _ in range(trials):
        kv_streaks = KvStreaks(list(random_permutation(n)))
        kv_streaks_count.append(len(kv_streaks))
    return sum(kv_streaks_count) / trials


def streak_lengths(n):
    counts = np.zeros((math.factorial(n) + 1, n + 1), dtype=int)
    perm_num = 0
    for kv_streaks in KvStreaks.generate_kv_streaks_for_all_permutations(n):
        perm_num += 1
        streaks = kv_streaks.kv_streaks
        for streak_length in streaks.values():
            counts[perm_num, streak_length] += 1
    return counts


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


def create_binary_array(arr):
    """
    Creates a binary array with 1s where arr is non-zero, and 0s otherwise.

    Args:
      arr: The input NumPy ndarray.

    Returns:
      A NumPy ndarray of the same shape, with 1s and 0s.
    """
    return (arr != 0).astype(int)


def complement_binary_array(arr):
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


if __name__ == "__main__":
    # for n in range(3, 7):
    #     print(f"{n}: {count_streak_lengths(n)}")
    # n = 100_000
    # print(mean_streaks(n, trials=100), math.log(n) + GAMMA)
    for n in range(5, 12):
        str_lens = streak_lengths(n)
        len_present = create_binary_array(str_lens)
        len_absent = complement_binary_array(len_present)
        all_perms = summarize_arr(str_lens)[SUMS][1]
        derangements = summarize_arr(len_absent)[SUMS][1]
        print(f"{n}: {all_perms / derangements}")
    # print(f"{summarize_arr(str_lens)=}")
    # print("=" * 20)
    # print(f"{summarize_arr(len_present)=}")
    # print("=" * 20)
    # print(f"{summarize_arr(len_absent)=}")
    # print(f"{summarize_arr(str_lens)[SUMS][1]=}")
    # print("=" * 20)
    # print(f"{summarize_arr(len_present)[SUMS][1]=}")
    # print("=" * 20)
    # print(f"{summarize_arr(len_absent)[SUMS][1]=}")
