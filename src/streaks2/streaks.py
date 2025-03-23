"""
This module contains classes for working with streaks of integers.
"""

from itertools import permutations
from math import factorial

import numpy as np
from termcolor import colored

from streaks2.utils import SUMS, summarize_arr


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
        # assert that the seq[0] is the minimum element
        if seq:
            assert min(seq) == seq[0]
        self.streak = seq

    def __repr__(self):
        return f"Streak({self.streak})"

    def __len__(self):
        """
        Returns the number of integers in the streak.
        """
        return len(self.streak)


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
        # assert that all elements in seq are distinct
        assert len(seq) == len(set(seq))
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
            return []

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

    def __len__(self):
        """
        Returns the number of streaks in the Streaks object.
        """
        return len(self.streaks)

    @classmethod
    def generate_streaks_for_all_permutations(cls, n):
        """
        Generates Streaks objects for every permutation of the integers from 1 to n (inclusive).

        Args:
            n (int): The upper limit of the range of integers to permute.

        Yields:
            Streaks: A Streaks object for each permutation.
        """
        for perm in permutations(range(1, n + 1)):
            yield cls(perm)  # Use cls() to create a Streaks object


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
        assert len(seq) == len(set(seq))
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

    def __len__(self):
        """
        Returns the number of streaks in the KvStreaks object.
        """
        return len(self.kv_streaks)

    @classmethod
    def generate_kv_streaks_for_all_permutations(cls, n):
        """
        Generates KvStreaks objects for every permutation of the integers from 1 to n (inclusive).

        Args:
            n (int): The upper limit of the range of integers to permute.

        Yields:
            KvStreaks: A KvStreaks object for each permutation.
        """
        for perm in permutations(range(1, n + 1)):
            yield cls(perm)  # Use cls() to create a KvStreaks object


class StrStats:
    def __init__(self, n):
        self.n = n
        self.streaks_arr = self._find_streaks_arr(n)
        self.counts = self._streak_counts()

    def _find_streaks_arr(self, n):
        lengths = self._streak_lengths(n)
        return summarize_arr(lengths)

    def _streak_lengths(self, n):
        length_counts = np.zeros((factorial(n) + 1, n + 1), dtype=int)
        perm_num = 0
        for kv_streaks in KvStreaks.generate_kv_streaks_for_all_permutations(n):
            perm_num += 1
            streaks = kv_streaks.kv_streaks
            for streak_length in streaks.values():
                length_counts[perm_num, streak_length] += 1
        return length_counts

    def _streak_counts(self):
        counts = np.zeros(self.n + 1, dtype=int)
        for i in range(1, factorial(self.n) + 1):
            counts[self.streaks_arr[i, SUMS]] += 1
        counts[SUMS] = sum(counts)
        return counts

    def by_length(self):
        """
        Returns the number of streaks by length.

        Returns:
            list: A list of integers representing the number of streaks by length.
        """
        return self.streaks_arr[SUMS, 1:]

    def by_count(self):
        """
        The number of permutations containing each streak count.

        Returns:
            list: A list of integers representing the number of streaks by count.
        """
        return self.counts[1:]

    def of_length(self, length):
        """
        Returns the number of streaks of a given length.

        Args:
            length (int): The length of the streak to count.

        Returns:
            int: The number of streaks of the given length.
        """
        return self.streaks_arr[SUMS, length]

    def of_count(self, count):
        """
        Returns the number of permutations that have the specified streak count.

        Args:
            count (int): The number of streaks in the permutation.

        Returns:
            int: The number of permutations with that many streaks.
        """
        return self.counts[count]

    def __repr__(self):
        return f"StrStats(n={self.n}, streaks_arr={self.streaks_arr})"

    def __str__(self):
        """Prints the array with arr[0] and arr[:, 0] in green using termcolor."""
        s = ""
        for i in range(self.streaks_arr.shape[0]):
            for j in range(self.streaks_arr.shape[1]):
                if i == 0 and j == 0:
                    s += colored(f"{self.streaks_arr[i, j]}", "red") + " "
                elif i == 0 or j == 0:
                    s += colored(f"{self.streaks_arr[i, j]}", "green") + " "
                else:
                    s += f"{self.streaks_arr[i, j]} "
            s += "\n"
        return s
