from math import factorial

import numpy as np
from sympy.functions.combinatorial.numbers import stirling

from streaks2.streaks import StrStats


def test_streak_counts_match_stirlings():
    """
    Test if the number of streaks of each length matches the Stirling numbers of the first kind.
    """
    for n in range(1, 10):
        streak_counts = StrStats(n).by_count()
        stirlings = np.array([stirling(n, i, kind=1) for i in range(1, n + 1)])
        assert np.array_equal(streak_counts, stirlings), (
            "Streaks do not match Stirlings"
        )


def test_streak_lengths_match_expected():
    """
    Test if the number of streaks of each length matches the expected values.
    """
    for n in range(1, 10):
        streak_lengths = StrStats(n).by_length()
        nperms = factorial(n)
        expected = np.zeros(n + 1, dtype=int)
        for length in range(1, n + 1):
            expected[length] = (
                nperms / length
            )  # number of streaks of given length should be n!/length
        expected = expected[1:]
        assert np.array_equal(streak_lengths, expected), (
            f"Streak lengths do not match expected for n={n}"
        )
