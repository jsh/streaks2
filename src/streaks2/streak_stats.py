from collections import Counter
from itertools import permutations

import streaks2.streaks as sts


# generate a random permutation of range(n)
def all_kv_streaks(n):
    for perm in permutations(range(1, n + 1)):
        kv_streaks = sts.KvStreaks(perm)
        yield kv_streaks.kv_streaks


def all_streaks(n):
    for perm in permutations(range(1, n + 1)):
        streaks = sts.Streaks(perm)
        yield streaks.streaks


# count len(streaks) across all permutations of range(1, n+1)
def streak_count(n):
    streak_counts = Counter()
    for streaks in all_streaks(n):
        streak_counts[len(streaks)] += 1
    return dict(sorted(streak_counts.items()))


def kv_streak_count(n):
    kv_streak_counts = Counter()
    for kv_streaks in all_kv_streaks(n):
        kv_streak_counts[len(kv_streaks)] += 1
    return dict(sorted(kv_streak_counts.items()))


# for i in range(9, 12):
#     start_time = time.perf_counter()
#     print(f"{streak_count(i)=}")
#     end_time = time.perf_counter()
#     elapsed_time = end_time - start_time
#     print(f"Elapsed time: {elapsed_time:.6f} seconds")
#     start_time = time.perf_counter()
#     print(f"{kv_streak_count(i)=}")
#     end_time = time.perf_counter()
#     elapsed_time = end_time - start_time
#     print(f"Elapsed time: {elapsed_time:.6f} seconds")


# start_time = time.perf_counter()
# kv_streaks = sts.KvStreaks(range(1, 1000001))
# print(f"{len(keys(kv_streaks))=}")
# end_time = time.perf_counter()
# elapsed_time = end_time - start_time
# print(f"Elapsed time: {elapsed_time:.6f} seconds")
