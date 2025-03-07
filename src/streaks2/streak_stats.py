from collections import Counter
from itertools import permutations

import streaks2.streaks as streaks


def count_streaks(n):
    streak_counts = Counter()
    for perm in permutations(range(1, n + 1)):
        streaks_list = streaks.find_streaks(perm)
        streak_counts[len(streaks_list)] += 1
    return dict(sorted(streak_counts.items()))


def mean_kv_streaks(n, trials=1):
    kv_streaks_count = []
    for _ in range(trials):
        kv_streaks = streaks.find_kv_streaks(streaks.random_permutation(n))
        kv_streaks_count.append(len(kv_streaks))
    return sum(kv_streaks_count) / trials


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
