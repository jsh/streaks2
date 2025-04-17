"""
This module contains classes for working with streaks of integers.
It provides functionality to represent, analyze, and generate statistics about streaks in permutations.
"""

from itertools import permutations
from math import factorial
from typing import Generator, List

import numpy as np
from termcolor import colored

from streaks2.utils import (
    SummaryIndex,
    add_summary_row_column,
    invert_zeros_and_nonzeros,
)

SUM = SummaryIndex.SUM.value


class Streak:
    """
    Represents a single streak of integers.
    """

    def __init__(self, seq: List[int]):
        """Initializes a Streak object.

        Args:
            seq (List[int]): A list of integers representing the streak.
                The first element should be the smallest.
        """
        if seq:
            if min(seq) != seq[0]:
                raise ValueError("Streak must start with the smallest element.")
        self.streak = seq

    def __repr__(self) -> str:
        return f"Streak({self.streak})"

    def __len__(self) -> int:
        """Returns the number of integers in the streak."""
        return len(self.streak)

    def __eq__(self, other: "Streak") -> bool:
        """
        Checks if two Streak objects are equal.

        Args:
            other (Streak): Another Streak object to compare.

        Returns:
            bool: True if the streaks are equal, False otherwise.
        """
        return self.streak == other.streak


class Streaks:
    """
    Represents a collection of Streak objects, decomposed from an integer sequence.
    """

    def __init__(self, seq: List[int]):
        """Initializes a Streaks object by decomposing a sequence of integers into streaks.

        Args:
            seq (List[int]): An integer sequence to decompose into streaks.
        """
        if len(seq) != len(set(seq)):
            raise ValueError("Sequence must contain distinct elements.")
        self.streaks = self._find_streaks(seq)

    def _find_streaks(self, seq: List[int]) -> List[Streak]:
        """Decomposes a list of integers into streaks.

        Args:
            seq (List[int]): A sequence of distinct integers.

        Returns:
            List[Streak]: A list of Streak objects.
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

    def __repr__(self) -> str:
        return f"Streaks({self.streaks})"

    def __len__(self) -> int:
        """Returns the number of streaks in the Streaks object."""
        return len(self.streaks)

    @classmethod
    def generate_streaks_for_all_permutations(
        cls, n: int
    ) -> Generator["Streaks", None, None]:
        """Generates Streaks objects for every permutation of the integers from 1 to n (inclusive).

        Args:
            n (int): The upper limit of the range of integers to permute.

        Yields:
            Generator["Streaks", None, None]: A Streaks object for each permutation.
        """
        for perm in permutations(range(1, n + 1)):
            yield cls(perm)


class KvStreaks:
    """
    Represents streaks as a dictionary of streak lengths, indexed by the first element of the streak.
    """

    def __init__(self, seq: List[int]):
        """Initializes a KvStreaks object.

        Args:
            seq (List[int]): A list of integers to analyze for streaks.
        """
        if len(seq) != len(set(seq)):
            raise ValueError("Sequence must contain distinct elements.")
        self.kv_streaks = {}
        self._find_kv_streaks(seq)

    def _find_kv_streaks(self, seq: List[int]):
        """Calculates the streak lengths and stores them in the kv_streaks dictionary.

        Args:
            seq (List[int]): A list of integers.
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

    def __repr__(self) -> str:
        return f"KvStreaks({self.kv_streaks})"

    def __len__(self) -> int:
        """Returns the number of streaks in the KvStreaks object."""
        return len(self.kv_streaks)

    @classmethod
    def generate_kv_streaks_for_all_permutations(
        cls, n: int
    ) -> Generator["KvStreaks", None, None]:
        """Generates KvStreaks objects for every permutation of the integers from 1 to n (inclusive).

        Args:
            n (int): The upper limit of the range of integers to permute.

        Yields:
            Generator["KvStreaks", None, None]: A KvStreaks object for each permutation.
        """
        for perm in permutations(range(1, n + 1)):
            yield cls(perm)


class StreakStatistics:
    """Calculates and stores statistics about streaks in permutations.

    This class provides methods to analyze the distribution of streak lengths and counts
    across all permutations of a given range of integers.
    """

    def __init__(self, n: int):
        """Initializes a StreakStatistics object for permutations of integers from 1 to n.

        Args:
            n (int): The upper limit of the range of integers to permute.
        """
        self.n = n
        self.streaks_arr = self._find_streaks_arr(n)
        self.sl_streak_counts = self._sl_streak_counts(n)
        self.counts = self._streak_counts()

    def _find_streaks_arr(self, n: int) -> np.ndarray:
        """Calculates and summarizes streak lengths for all permutations.

        Args:
            n (int): The upper limit of the range of integers to permute.

        Returns:
            np.ndarray: A NumPy array summarizing the streak lengths.
        """
        lengths = self._streak_lengths(n)
        return add_summary_row_column(lengths)

    def _streak_lengths(self, n: int) -> np.ndarray:
        """Calculates the streak lengths for all permutations of integers from 1 to n."""
        length_counts = np.zeros((factorial(n) + 1, n + 1), dtype=int)
        perm_num = 0
        for kv_streaks in KvStreaks.generate_kv_streaks_for_all_permutations(n):
            perm_num += 1
            streaks = kv_streaks.kv_streaks
            for streak_length in streaks.values():
                length_counts[perm_num, streak_length] += 1
        return length_counts

    def _streak_counts(self) -> np.ndarray:
        """Counts the number of permutations with each streak count."""
        counts = np.zeros(self.n + 1, dtype=int)
        for i in range(1, factorial(self.n) + 1):
            counts[self.streaks_arr[i, SUM]] += 1
        counts[SUM] = sum(counts)
        return counts

    def _sl_streak_counts(self, n: int) -> np.ndarray:
        counts = np.zeros((n + 1, n + 1), dtype=int)
        for kv_streaks in KvStreaks.generate_kv_streaks_for_all_permutations(n):
            streaks = kv_streaks.kv_streaks
            for start, length in streaks.items():
                counts[start, length] += 1
        counts[SUM] = np.sum(counts, axis=0)
        counts[:, SUM] = np.sum(counts, axis=1)
        counts[SUM, SUM] = np.sum(counts[1:, 1:])
        return counts

    def by_length(self) -> np.ndarray:
        """
        Returns the number of streaks by length.
        """
        return self.streaks_arr[SUM, 1:]

    def by_count(self) -> np.ndarray:
        """
        The number of permutations containing each streak count.
        """
        return self.counts[1:]

    def of_length(self, length: int) -> int:
        """
        Returns the number of streaks of a given length.
        """
        return self.streaks_arr[SUM, length]

    def of_count(self, count: int) -> int:
        """
        Returns the number of permutations that have the specified streak count.
        """
        return self.counts[count]

    def _streak_length_absent(self) -> np.ndarray:
        """Inverts zeros and nonzeros in the streaks array and summarizes the result."""
        absent = invert_zeros_and_nonzeros(self.streaks_arr)
        return add_summary_row_column(absent)

    def missing_streak_lengths(self) -> int:
        """Calculates the number of missing streak lengths."""
        return self._streak_length_absent()[0]

    def __repr__(self) -> str:
        """Returns a string representation of the StreakStatistics object."""
        return f"StreakStatistics(n={self.n}, streaks_arr={self.streaks_arr})"

    def __str__(self) -> str:
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
