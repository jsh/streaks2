import numpy as np
import pytest

from streaks2.streaks import find_kv_streaks, find_streaks, random_permutation


def test_random_permutation():
    n = 10
    perm = random_permutation(n)
    assert len(perm) == n
    assert sorted(perm) == list(range(n))


def test_find_streaks():
    assert find_streaks([]) == []
    assert find_streaks([1]) == [[1]]
    assert find_streaks([1, 2, 3]) == [[1, 2, 3]]
    assert find_streaks([3, 2, 1]) == [[3], [2], [1]]
    assert find_streaks([2, 1, 3]) == [[2], [1, 3]]
    assert find_streaks([1, 3, 2, 4]) == [[1, 3, 2, 4]]


def test_kv_streaks():
    assert find_kv_streaks(np.array([])) == {}
    assert find_kv_streaks(np.array([1])) == {1: 1}
    assert find_kv_streaks(np.array([1, 2, 3])) == {1: 3}
    assert find_kv_streaks(np.array([3, 2, 1])) == {3: 1, 2: 1, 1: 1}
    assert find_kv_streaks(np.array([2, 1, 3])) == {2: 1, 1: 2}
    assert find_kv_streaks(np.array([1, 3, 2, 4])) == {1: 4}


if __name__ == "__main__":
    pytest.main()
