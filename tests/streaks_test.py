import numpy as np
import pytest

from streaks2.streaks import KvStreaks, Streak, Streaks, StreakStatistics


def test_streak_init_valid():
    """Test that a Streak object is initialized correctly with a valid sequence."""
    streak = Streak([1, 2, 3])
    assert streak.streak == [1, 2, 3]


def test_streak_init_invalid():
    """Test that a Streak object raises a ValueError when initialized with an invalid sequence."""
    with pytest.raises(
        ValueError, match=r"^Streak must start with the smallest element.$"
    ):
        Streak([2, 1, 3])


def test_streak_len():
    """Test the __len__() method of the Streak class."""
    streak = Streak([1, 2, 3])
    assert len(streak) == 3
    streak = Streak([])
    assert len(streak) == 0


def test_find_kv_streaks_empty_seq():
    """Test that _find_kv_streaks handles an empty sequence."""
    kv_streaks = KvStreaks([])
    assert kv_streaks.kv_streaks == {}


def test_streak_length_absent():
    """Test that _streak_length_absent returns the correct array."""
    n = 3
    stats = StreakStatistics(n)
    absent_arr = stats._streak_length_absent()
    assert absent_arr.shape == (7, 4)


def test_missing_streak_lengths():
    """Test that missing_streak_lengths returns the correct count."""
    n = 3
    stats = StreakStatistics(n)
    observed = stats.missing_streak_lengths()
    expected = np.array([9, 2, 3, 4])
    assert np.array_equal(observed, expected)


def test_find_streaks_empty_seq():
    """Test that _find_streaks returns an empty list when given an empty sequence."""
    streaks = Streaks([])
    assert streaks._find_streaks([]) == []


def test_streaks_repr():
    """Test the __repr__() method of the Streaks class."""
    streaks = Streaks([1, 2, 3, 4])
    assert repr(streaks).startswith("Streaks([Streak([1, 2, 3, 4])")


def test_kvstreaks_repr():
    """Test the __repr__() method of the KvStreaks class."""
    kvstreaks = KvStreaks([1, 2, 3, 4])
    assert repr(kvstreaks) == "KvStreaks({1: 4})"


def test_streaks_init_valid():
    """Test that a Streaks object is initialized correctly with a valid sequence."""
    streaks = Streaks([1, 2, 3, 4])
    assert len(streaks.streaks) > 0


def test_streaks_init_invalid():
    """Test that a Streaks object raises a ValueError when initialized with an invalid sequence."""
    with pytest.raises(ValueError, match=r"^Sequence must contain distinct elements.$"):
        Streaks([1, 2, 2, 3])


def test_kvstreaks_init_valid():
    """Test that a KvStreaks object is initialized correctly with a valid sequence."""
    kvstreaks = KvStreaks([1, 2, 3, 4])
    assert len(kvstreaks.kv_streaks) > 0


def test_kvstreaks_init_invalid():
    """Test that a KvStreaks object raises a ValueError when initialized with an invalid sequence."""
    with pytest.raises(ValueError, match=r"^Sequence must contain distinct elements.$"):
        KvStreaks([1, 2, 2, 3])


def test_streak_eq():
    """Test that two Streak objects are equal when they have the same sequence."""
    streak1 = Streak([1, 2, 3])
    streak2 = Streak([1, 2, 3])
    assert streak1 == streak2


def test_streak_not_eq():
    """Test that two Streak objects are not equal when they have different sequences."""
    streak1 = Streak([1, 2, 3])
    streak2 = Streak([1, 3, 2])
    assert streak1 != streak2


def test_streaks_len():
    """Test that the len() method returns the correct number of streaks."""
    streaks = Streaks([4, 1, 2, 3])
    assert len(streaks) == 2


def test_kvstreaks_len():
    """Test that the len() method returns the correct number of kv_streaks."""
    kvstreaks = KvStreaks([4, 1, 2, 3])
    assert len(kvstreaks) == 2


def test_streaks_generate_streaks_for_all_permutations():
    """Test that the generate_streaks_for_all_permutations() method generates the correct number of Streaks objects."""
    n = 3
    streaks_generator = Streaks.generate_streaks_for_all_permutations(n)
    streaks_list = list(streaks_generator)
    assert len(streaks_list) == 6  # 3! = 6


def test_kvstreaks_generate_kv_streaks_for_all_permutations():
    """Test that the generate_kv_streaks_for_all_permutations() method generates the correct number of KvStreaks objects."""
    n = 3
    kvstreaks_generator = KvStreaks.generate_kv_streaks_for_all_permutations(n)
    kvstreaks_list = list(kvstreaks_generator)
    assert len(kvstreaks_list) == 6  # 3! = 6


def test_str_stats_initialization():
    n = 3
    stats = StreakStatistics(n)
    assert stats.n == n
    assert stats.streaks_arr.shape == (7, 4)  # factorial(3) + 1, 3 + 1
    assert stats.counts.shape == (4,)


def test_str_stats_by_length():
    n = 3
    stats = StreakStatistics(n)
    assert len(stats.by_length()) == n


def test_str_stats_by_count():
    n = 3
    stats = StreakStatistics(n)
    assert len(stats.by_count()) == n


def test_str_stats_of_length():
    n = 3
    stats = StreakStatistics(n)
    assert stats.of_length(1) == 6
    assert stats.of_length(2) == 3
    assert stats.of_length(3) == 2


def test_str_stats_of_count():
    n = 3
    stats = StreakStatistics(n)
    assert stats.of_count(1) == 2
    assert stats.of_count(2) == 3
    assert stats.of_count(3) == 1


def test_str_stats_repr():
    n = 3
    stats = StreakStatistics(n)
    assert repr(stats).startswith("StreakStatistics(n=3, streaks_arr=")


def test_str_stats_str():
    n = 3
    stats = StreakStatistics(n)
    assert isinstance(str(stats), str)
