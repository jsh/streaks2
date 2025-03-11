# import numpy as np
# import sympy

# GAMMA = float(sympy.S.EulerGamma)


# # generate a random permutation of range(n)
# def random_permutation(n):
#     """
#     Generate a random permutation of integers from 0 to n-1.

#     Args:
#         n (int): The upper limit (exclusive) for the range of integers to permute.

#     Returns:
#         list: A list containing a random permutation of integers from 0 to n-1.
#     """
#     return np.random.permutation(n)


class Streak:
    """
    Represents a single streak of integers.
    """

    def __init__(self, seq):
        """
        Initializes a Streak object.

        Args:
            seq (list): A list of integers representing the streak.
                                 The first element should be the smallest.
        """
        self.streak = seq

    def __repr__(self):
        return f"Streak({self.streak})"


class Streaks:
    """
    Represents a collection of Streak objects, decomposed from an integer sequence.
    """

    def __init__(self, seq):
        """
        Initializes a Streaks object by decomposing a sequence of integers into streaks.

        Args:
            seq (list): An integer sequence to decompose into streaks.
        """
        self.streaks = self._find_streaks(seq)

    def _find_streaks(self, seq):
        """
        Decomposes a list of integers into streaks.

        Args:
            seq (list): A sequence of distinct integers.

        Returns:
            list: A list of Streak objects.
        """
        if not seq:
            return [Streak([])]

        streaks = []
        current_streak = [seq[0]]

        for i in range(1, len(seq)):
            if seq[i] >= current_streak[0]:
                current_streak.append(seq[i])
            else:
                streaks.append(Streak(current_streak))
                current_streak = [seq[i]]

        streaks.append(Streak(current_streak))
        return streaks

    def __repr__(self):
        return f"Streaks({self.streaks})"


class KvStreaks:
    """
    Represents streaks as a dictionary of streak lengths, indexed by the first element of the streak.
    """

    def __init__(self, seq):
        """
        Initializes a KvStreaks object.

        Args:
            seq (list): A list of integers to analyze for streaks.
        """
        self.kv_streaks = {}
        self._find_kv_streaks(seq)

    def _find_kv_streaks(self, seq):
        """
        Calculates the streak lengths and stores them in the kv_streaks dictionary.

        Args:
            seq (list): A list of integers.
        """
        if not seq:
            return

        streak_start = seq[0]
        streak_length = 1

        for i in range(1, len(seq)):
            if seq[i] > streak_start:
                streak_length += 1
            else:
                self.kv_streaks[int(streak_start)] = streak_length
                streak_start = seq[i]
                streak_length = 1

        self.kv_streaks[int(streak_start)] = streak_length

    def __repr__(self):
        return f"KvStreaks({self.kv_streaks})"


# def first_kv_streak(seq):
#     """
#     Return the first key-value pair of the streaks in seq.

#     Args:
#         seq (list): A list of distinct integers.

#     Returns:
#         a tuple of the first key-value pair of the streaks in seq.
#     """
#     if (type(seq) is np.ndarray) and (not seq.any()):
#         return ()
#     elif (type(seq) is list) and (not seq):
#         return ()

#     streak_start = seq[0]
#     streak_length = 1

#     for i in range(1, len(seq)):
#         if seq[i] > streak_start:
#             streak_length += 1
#         else:
#             break

#     return (int(streak_start), streak_length)


# def streak_count_by_start(n):
#     """
#     Count how many streaks start with each integer, over all permutations.

#     Args:
#         n (int): The number of elements to permute.
#         The permutations will be of the integers from 1 to n.

#     Returns:
#         A dictionary counting the number of permutations
#         for which each integer starts a streak.
#         This should be {k: n!/k} for k in 1..n.
#     """
#     starts = Counter()
#     for perm in permutations(range(1, n + 1)):
#         kv_streaks = KvStreaks(perm)
#         starts_in_perm = kv_streaks.kv_streaks.keys()
#         starts += Counter(starts_in_perm)
#     return dict(starts)


# def total_streak_length_by_start(n):
#     """
#     Count the total length of streaks starting with each integer, over all permutations.

#     Returns:
#         A dictionary counting the total length of streaks starting with each integer.
#         This turns out to be {k: (n+1)!/(k+1)*k} for k in 1..n.
#     """
#     lengths = Counter()
#     for perm in permutations(range(1, n + 1)):
#         kv_streaks = KvStreaks(perm)
#         lengths += Counter(kv_streaks.kv_streaks)
#     return {k: v for k, v in lengths.items()}
