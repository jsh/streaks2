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
