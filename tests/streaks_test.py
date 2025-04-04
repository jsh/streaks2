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
