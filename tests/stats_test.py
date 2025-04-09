from math import exp, factorial

import numpy as np
from sympy.functions.combinatorial.numbers import stirling

from streaks2.streaks import StreakStatistics
from streaks2.utils import create_array_from_kv


def test_streak_counts_match_stirlings() -> None:
    """
    Test if the number of streaks of each length matches the Stirling numbers of the first kind.
    """
    for n in range(1, 10):
        streak_counts = StreakStatistics(n).by_count()
        stirlings = np.array([stirling(n, i, kind=1) for i in range(1, n + 1)])
        assert np.array_equal(streak_counts, stirlings), (
            "Streaks do not match Stirlings"
        )


def test_streak_lengths_match_expected() -> None:
    """
    Test if the number of streaks of each length matches the expected values.
    """
    for n in range(1, 10):
        streak_lengths = StreakStatistics(n).by_length()
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


# def test_missing_streak_lengths():
#     # Compare the number of missing streak lengths with the expected values
#     # based on the Poisson distribution.
#     for n in range(4, 10):
#         # [derangements, permutations lacking transpositions, lacking 3 cycles, etc.]
#         observed = StreakStatistics(n).missing_streak_lengths()[1:]
#         # The expected number of missing streak lengths is given by the formula:
#         # E[X] = n! * exp(-1/k) for k = 1, 2, ..., n
#         poisson_p_zeros = np.exp(-1 / np.arange(1, n + 1))
#         expected = factorial(n) * poisson_p_zeros
#         # This should actually be done with a Student's t-test.
#         #rel_error = np.abs((observed - expected) / expected)
#         # assert np.all(rel_error < 0.1)
#         # TODO: replace with a chi-squared test.


def test_dist_of_singletons() -> None:
    """
    Test the distribution of singletons across permutations.
    These should follow a Poisson distribution.
    The expected number of singletons is given by the formula:
    E[k] = n! * exp(-1)/k! for k = 1, 2, ..., n
    where k is the number of singletons.
    """
    n = 7
    # TODO: Add a range of n values.
    singletons = StreakStatistics(n).streaks_arr[1:, 1]
    unique_vals, counts = np.unique(singletons, return_counts=True)
    observed = create_array_from_kv(unique_vals, counts)
    factorials = np.array([factorial(i) for i in range(0, n + 1)])
    expected = factorial(n) / (exp(1) * factorials)
    expected[-1] = sum(observed) - sum(expected[:-1])

    # print(f"Expected: {expected}")
    # return expected
    # print(f"Observed: {observed}")
    # TODO: This, too, needs a chi-squared test.
    pass
