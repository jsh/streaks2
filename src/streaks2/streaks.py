from collections import Counter
from itertools import permutations

import numpy as np
import sympy

GAMMA = float(sympy.S.EulerGamma)


# generate a random permutation of range(n)
def random_permutation(n):
    """
    Generate a random permutation of integers from 0 to n-1.

    Args:
        n (int): The upper limit (exclusive) for the range of integers to permute.

    Returns:
        list: A list containing a random permutation of integers from 0 to n-1.
    """
    return np.random.permutation(n)


def find_streaks(lst):
    """
    Decompose lst into streaks. A streak is a sequence of integers, all of which are are larger than the initial integer of the streak.

    Args:
        lst (list): A list of distinct integers.

    Returns:
        list: A list of sublists, where each sublist is a streak.

    Examples:
        find_streaks([1]) -> [[1]]
        find_streaks([1, 2, 3]) -> [[1, 2, 3]]
        find_streaks([3, 2, 1]) -> [[3], [2], [1]]
        find_streaks([2, 1, 3]) -> [[2], [1, 3]]
    """

    if not lst:
        return []

    streaks = []
    current_streak = [lst[0]]

    for i in range(1, len(lst)):
        if lst[i] >= current_streak[0]:
            current_streak.append(lst[i])
        else:
            streaks.append(current_streak)
            current_streak = [lst[i]]

    streaks.append(current_streak)
    return streaks


def find_kv_streaks(lst):
    """
    Find the lengths of all streaks in a list of integers and return them as a dictionary.

    Args:
        lst (list): A list or ndarray of distinct integers.

    Returns:
        dict: A dictionary where the keys are the starting integers of each streak and the values are the lengths of those streaks.
    """
    kv_streaks = {}
    if (type(lst) is np.ndarray) and (not lst.any()):
        return kv_streaks
    elif (type(lst) is list) and (not lst):
        return kv_streaks

    streak_start = lst[0]
    streak_length = 1

    for i in range(1, len(lst)):
        if lst[i] > streak_start:
            streak_length += 1
        else:
            kv_streaks[int(streak_start)] = streak_length
            streak_start = lst[i]
            streak_length = 1

    kv_streaks[streak_start] = streak_length
    return kv_streaks


def first_kv_streak(lst):
    """
    Return the first key-value pair of the streaks in lst.

    Args:
        lst (list): A list of distinct integers.

    Returns:
        a tuple of the first key-value pair of the streaks in lst.
    """
    if (type(lst) is np.ndarray) and (not lst.any()):
        return ()
    elif (type(lst) is list) and (not lst):
        return ()

    streak_start = lst[0]
    streak_length = 1

    for i in range(1, len(lst)):
        if lst[i] > streak_start:
            streak_length += 1
        else:
            break

    return (int(streak_start), streak_length)


def streak_count_by_start(n):
    """
    Count how many streaks start with each integer, over all permutations.

    Args:
        n (int): The number of elements to permute.
        The permutations will be of the integers from 1 to n.

    Returns:
        A dictionary counting the number of permutations
        for which each integer starts a streak.
        This turns out to be {k: n!/k} for k in 1..n.


    Examples:
        streak_count_by_start(1) -> {1: 1}
        streak_count_by_start(2) -> {1: 2, 2: 1}
        streak_count_by_start(3) -> {1: 6, 2: 3, 3: 2}
        streak_count_by_start(4) -> {1: 24, 2: 12, 3: 8, 4: 6}
    """
    starts = Counter()
    for perm in permutations(range(1, n + 1)):
        starts_in_perm = find_kv_streaks(perm).keys()
        starts += Counter(starts_in_perm)
    return dict(starts)


def total_streak_length_by_start(n):
    """
    Count the total length of streaks starting with each integer, over all permutations.

    Returns:
        A dictionary counting the total length of streaks starting with each integer.
        This turns out to be {k: (n+1)!/(k+1)*k} for k in 1..n.


    Examples:
        total_streak_length_by_start(1) -> {1: 1}
        total_streak_length_by_start(2) -> {1: 3, 2: 1}
        total_streak_length_by_start(3) -> {1: 12, 2: 4, 3: 2}
        total_streak_length_by_start(4) -> {1: 60, 2: 20, 3: 10, 4: 6}

    """
    lengths = Counter()
    for perm in permutations(range(1, n + 1)):
        streaks = find_kv_streaks(np.array(perm))
        lengths += Counter(streaks)
    return {k: v for k, v in lengths.items()}
