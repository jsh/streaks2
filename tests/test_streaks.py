import pytest
from expt.streaks import random_permutation, find_streaks, kv_streaks
import numpy as np

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
    assert kv_streaks(np.array([])) == {}
    assert kv_streaks(np.array([1])) == {1: 1}
    assert kv_streaks(np.array([1, 2, 3])) == {1: 3}
    assert kv_streaks(np.array([3, 2, 1])) == {3: 1, 2: 1, 1: 1}
    assert kv_streaks(np.array([2, 1, 3])) == {2: 1, 1: 2}
    assert kv_streaks(np.array([1, 3, 2, 4])) == {1: 4}

if __name__ == "__main__":
    pytest.main()