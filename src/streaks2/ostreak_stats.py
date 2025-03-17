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
