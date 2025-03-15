import pytest

from streaks2.streaks import KvStreaks, Streak, Streaks


def test_streak_initialization():
    s = Streak([1, 2, 3])
    assert s.streak == [1, 2, 3]


def test_streak_repr():
    s = Streak([1, 2, 3])
    assert repr(s) == "Streak([1, 2, 3])"


def test_streaks_initialization():
    s = Streaks([1, 2, 3, 4, 5])
    assert len(s.streaks) == 1
    assert s.streaks[0].streak == [1, 2, 3, 4, 5]


def test_streaks_repr():
    s = Streaks([1, 2, 3, 4, 5])
    assert repr(s) == "Streaks([Streak([1, 2, 3, 4, 5])])"


def test_kv_streaks_initialization():
    kv = KvStreaks([1, 2, 3, 4, 5])
    assert kv.kv_streaks == {1: 5}


def test_kv_streaks_repr():
    kv = KvStreaks([1, 2, 3, 4, 5])
    assert repr(kv) == "KvStreaks({1: 5})"


def test_empty_streak():
    s = Streak([])
    assert s.streak == []


def test_empty_streaks():
    s = Streaks([])
    assert s.streaks == []


def test_empty_kv_streaks():
    kv = KvStreaks([])
    assert kv.kv_streaks == {}


def test_streaks_with_non_consecutive_numbers():
    s = Streaks([5, 1, 3, 2, 4])
    assert len(s.streaks) == 2
    assert s.streaks[0].streak == [5]
    assert s.streaks[1].streak == [1, 3, 2, 4]


def test_kv_streaks_with_non_consecutive_numbers():
    kv = KvStreaks([5, 1, 3, 2, 4])
    assert kv.kv_streaks == {5: 1, 1: 4}


def test_streak_initialization_with_non_minimum_first_element():
    with pytest.raises(AssertionError):
        Streak([2, 1, 3])


def test_streaks_initialization_with_duplicates():
    with pytest.raises(AssertionError):
        Streaks([1, 2, 2, 3, 4])


def test_kv_streaks_initialization_with_duplicates():
    with pytest.raises(AssertionError):
        KvStreaks([1, 2, 2, 3, 4])


def test_streaks_with_decreasing_numbers():
    s = Streaks([5, 4, 3, 2, 1])
    assert len(s.streaks) == 5
    assert s.streaks[0].streak == [5]
    assert s.streaks[1].streak == [4]
    assert s.streaks[2].streak == [3]
    assert s.streaks[3].streak == [2]
    assert s.streaks[4].streak == [1]


def test_kv_streaks_with_decreasing_numbers():
    kv = KvStreaks([5, 4, 3, 2, 1])
    assert kv.kv_streaks == {5: 1, 4: 1, 3: 1, 2: 1, 1: 1}


def test_streaks_len():
    s = Streaks([1, 2, 3, 4, 5])
    assert len(s) == 1
    s = Streaks([5, 1, 3, 2, 4])
    assert len(s) == 2
    s = Streaks([])
    assert len(s) == 0


def test_kv_streaks_len():
    kv = KvStreaks([1, 2, 3, 4, 5])
    assert len(kv) == 1
    kv = KvStreaks([5, 1, 3, 2, 4])
    assert len(kv) == 2
    kv = KvStreaks([])
    assert len(kv) == 0


def test_streak_len():
    s = Streak([1, 2, 3, 4, 5])
    assert len(s) == 5
    s = Streak([5])
    assert len(s) == 1
    s = Streak([])
    assert len(s) == 0

    def test_streaks_generate_streaks_for_all_permutations():
        n = 3
        streaks_list = list(Streaks.generate_streaks_for_all_permutations(n))
        assert len(streaks_list) == 6  # 3! = 6 permutations
        for streaks in streaks_list:
            assert isinstance(streaks, Streaks)

    def test_kv_streaks_generate_kv_streaks_for_all_permutations():
        n = 3
        kv_streaks_list = list(KvStreaks.generate_kv_streaks_for_all_permutations(n))
        assert len(kv_streaks_list) == 6  # 3! = 6 permutations
        for kv_streaks in kv_streaks_list:
            assert isinstance(kv_streaks, KvStreaks)
