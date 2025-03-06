import math

from sympy.functions.combinatorial.numbers import stirling

from streaks2.streak_stats import count_streaks, mean_kv_streaks
from streaks2.streaks import GAMMA


def test_count_streaks():
    for n in range(1, 10):
        stirlings = {i: stirling(n, i, kind=1) for i in range(1, n + 1)}
        assert count_streaks(n) == stirlings


def test_mean_kv_streaks():
    n = 1_000
    trials = 100
    mean_kv = mean_kv_streaks(n, trials)
    expected = math.log(n) + GAMMA
    assert math.isclose(mean_kv, expected, rel_tol=0.1)
