import numpy as np
import sympy

GAMMA = float(sympy.S.EulerGamma)


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


# def first_kv_streak(seq):
#     """
#     Return the first key-value pair of the streaks in seq.

#     Args:
#         seq (list): A list of distinct integers.

#     Returns:
#         a tuple of the first key-value pair of the streaks in seq.
#     """
#     if (type(seq) is np.ndarray) and (not seq.any()):
#         return ()
#     elif (type(seq) is list) and (not seq):
#         return ()

#     streak_start = seq[0]
#     streak_length = 1

#     for i in range(1, len(seq)):
#         if seq[i] > streak_start:
#             streak_length += 1
#         else:
#             break

#     return (int(streak_start), streak_length)


# def streak_count_by_start(n):
#     """
#     Count how many streaks start with each integer, over all permutations.

#     Args:
#         n (int): The number of elements to permute.
#         The permutations will be of the integers from 1 to n.

#     Returns:
#         A dictionary counting the number of permutations
#         for which each integer starts a streak.
#         This should be {k: n!/k} for k in 1..n.
#     """
#     starts = Counter()
#     for perm in permutations(range(1, n + 1)):
#         kv_streaks = KvStreaks(perm)
#         starts_in_perm = kv_streaks.kv_streaks.keys()
#         starts += Counter(starts_in_perm)
#     return dict(starts)


# def total_streak_length_by_start(n):
#     """
#     Count the total length of streaks starting with each integer, over all permutations.

#     Returns:
#         A dictionary counting the total length of streaks starting with each integer.
#         This turns out to be {k: (n+1)!/(k+1)*k} for k in 1..n.
#     """
#     lengths = Counter()
#     for perm in permutations(range(1, n + 1)):
#         kv_streaks = KvStreaks(perm)
#         lengths += Counter(kv_streaks.kv_streaks)
#     return {k: v for k, v in lengths.items()}
