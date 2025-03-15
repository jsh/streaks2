"""
This module contains classes for working with streaks of integers.
"""

from itertools import permutations


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


# Example usage:
if __name__ == "__main__":
    n = 3
    for kv_streaks in KvStreaks.generate_kv_streaks_for_all_permutations(n):
        print(kv_streaks)
