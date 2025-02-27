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
