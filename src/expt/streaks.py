from itertools import permutations
import math
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

def kv_streaks(lst):
    """
    Find the lengths of all streaks in a list of integers and return them as a dictionary.

    Args:
        lst (list): A list of distinct integers.

    Returns:
        dict: A dictionary where the keys are the starting integers of each streak and the values are the lengths of those streaks.
    """
    kv_streaks = {}
    if not lst.any():
        return kv_streaks

    streak_start = lst[0]
    streak_length = 1

    for i in range(1, len(lst)):
        if lst[i] > streak_start:
            streak_length += 1
        else:
            kv_streaks[streak_start] = streak_length
            streak_start = lst[i]
            streak_length = 1

    kv_streaks[streak_start] = streak_length
    return kv_streaks

"""
n = 10
tot_len = 0

for perm in permutations(range(1, n+1)):
    s = find_streaks(perm)
    #print(s)
    l = len(s)
    tot_len += l
print(tot_len/math.factorial(n))
print(math.log(n) + GAMMA)

print("---------------------------------")

# tot_len = 0
# for perm in permutations(range(1, n+1)):
#     kvs = kv_streaks(perm)
#     #print(s)
#     l = len(kvs)
#     tot_len += l
# print(tot_len/math.factorial(n))
# print(math.log(n) + GAMMA)

# print("---------------------------------")

lst = random_permutation(1_000_000)
# #print(find_streaks(lst))
print(len(kv_streaks(lst)))
"""