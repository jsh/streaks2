import math
from collections import Counter

from streaks2.streaks import KvStreaks
from streaks2.utils import GAMMA, random_permutation


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


if __name__ == "__main__":
    # for n in range(3, 7):
    #     print(f"{n}: {count_streak_lengths(n)}")
    n = 100_000
    print(mean_streaks(n, trials=100), math.log(n) + GAMMA)
