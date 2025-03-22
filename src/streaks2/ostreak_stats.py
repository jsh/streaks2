"""
from collections import Counter
from itertools import permutations

import streaks2.streaks as streaks


# count all streaks of length l in all permutations of range(1, n+1)
# return a dictionary with the counts of each length
# count_streaks(3) -> {1: 6, 2: 3, 3: 1}
# count_streaks(4) -> {1: 24, 2: 12, 3: 6, 4: 1}
def count_streaks_by_length(n):
    streak_counts = Counter()
    for perm in permutations(range(1, n + 1)):
        streaks_list = streaks.find_streaks(perm)
        for streak in streaks_list:
            streak_counts[len(streak)] += 1
    return dict(sorted(streak_counts.items()))
"""
# def print_kv_streaks(n):
#     for kv_streaks in KvStreaks.generate_kv_streaks_for_all_permutations(n):
#         print(kv_streaks)


# def count_streak_lengths(n):
#     streak_length_counts = Counter()
#     for kv_streaks in KvStreaks.generate_kv_streaks_for_all_permutations(n):
#         streak_length_counts[len(kv_streaks)] += 1
#     return dict(sorted(streak_length_counts.items()))


# def mean_streaks(n, trials=1):
#     kv_streaks_count = []
#     for _ in range(trials):
#         kv_streaks = KvStreaks(list(random_permutation(n)))
#         kv_streaks_count.append(len(kv_streaks))
#     return sum(kv_streaks_count) / trials
