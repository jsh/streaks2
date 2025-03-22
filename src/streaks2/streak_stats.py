import math
from collections import Counter

import numpy as np

from streaks2.streaks import KvStreaks
from streaks2.utils import random_permutation, summarize_arr


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


class StrStats:
    """
    Represents streaks as a dictionary of streak lengths, indexed by the first element of the streak.
    """

    def __init__(self, n):
        """
        .
        """
        self.n = n
        self.streaks_arr = self._find_streaks_arr(n)

    def _find_streaks_arr(self, n):
        lengths = self._streak_lengths(n)
        return summarize_arr(lengths)

    def _streak_lengths(self, n):
        length_counts = np.zeros((math.factorial(n) + 1, n + 1), dtype=int)
        perm_num = 0
        for kv_streaks in KvStreaks.generate_kv_streaks_for_all_permutations(n):
            perm_num += 1
            streaks = kv_streaks.kv_streaks
            for streak_length in streaks.values():
                length_counts[perm_num, streak_length] += 1
        return length_counts

    def __repr__(self):
        return f"KvStreaksStats(n={self.n}, streaks_arr={self.streaks_arr})"


if __name__ == "__main__":
    # for n in range(3, 7):
    #     print(f"{n}: {count_streak_lengths(n)}")
    # n = 100_000
    # print(mean_streaks(n, trials=100), math.log(n) + GAMMA)
    for n in range(2, 6):
        print(StrStats(n))
        # str_lens = streak_lengths(n)
        # len_present = create_binary_array(str_lens)
        # len_absent = complement_binary_array(len_present)
        # all_perms = summarize_arr(str_lens)[SUMS][1]
        # derangements = summarize_arr(len_absent)[SUMS][1]
        # print(f"{n}: {all_perms / derangements}")
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
