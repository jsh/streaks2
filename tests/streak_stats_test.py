"""
import math

from sympy.functions.combinatorial.numbers import stirling

from streaks2.streak_stats import (
    count_streaks,
    count_streaks_by_length,
    mean_kv_streaks,
)
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


# write pytest unit tests of count_streaks_by_length(n)
# in the dictionary the function returns,
# for each key, k, the expected value is n!/k.
# Write tests for n = range(1, 10)


def test_count_streaks_by_length():
    for n in range(1, 10):
        streaks_by_length = count_streaks_by_length(n)
        for k in streaks_by_length:
            expected_value = math.factorial(n) / k
            assert streaks_by_length[k] == expected_value


def test_all_lines_in_permutation_block_same_length():
    n = 5
    n_fact = math.factorial(n)
    streaks_by_length = count_streaks_by_length(n)
    for k in streaks_by_length:
        assert k * streaks_by_length[k] == n_fact
"""
