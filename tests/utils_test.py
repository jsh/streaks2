import numpy as np
import pytest

from streaks2.streaks import (
    first_kv_streak,
    random_permutation,
    streak_count_by_start,
    total_streak_length_by_start,
)


def test_random_permutation():
    n = 10
    perm = random_permutation(n)
    assert len(perm) == n
    assert sorted(perm) == list(range(n))


def test_first_kv_streak():
    assert first_kv_streak(np.array([])) == ()
    assert first_kv_streak(np.array([1])) == (1, 1)
    assert first_kv_streak(np.array([1, 2, 3])) == (1, 3)
    assert first_kv_streak(np.array([3, 2, 1])) == (3, 1)
    assert first_kv_streak(np.array([2, 1, 3])) == (2, 1)
    assert first_kv_streak(np.array([1, 3, 2, 4])) == (1, 4)


def test_streak_inits():
    assert streak_count_by_start(1) == {1: 1}
    assert streak_count_by_start(2) == {1: 2, 2: 1}
    assert streak_count_by_start(3) == {1: 6, 2: 3, 3: 2}
    assert streak_count_by_start(4) == {1: 24, 2: 12, 3: 8, 4: 6}
    assert streak_count_by_start(5) == {1: 120, 2: 60, 3: 40, 4: 30, 5: 24}


def test_total_streak_length_by_start():
    assert total_streak_length_by_start(1) == {1: 1}
    assert total_streak_length_by_start(2) == {1: 3, 2: 1}
    assert total_streak_length_by_start(3) == {1: 12, 2: 4, 3: 2}
    assert total_streak_length_by_start(4) == {1: 60, 2: 20, 3: 10, 4: 6}
    assert total_streak_length_by_start(5) == {1: 360, 2: 120, 3: 60, 4: 36, 5: 24}


if __name__ == "__main__":
    pytest.main()
