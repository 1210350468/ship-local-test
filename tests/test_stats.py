import pytest

from stats import mean


def test_mean():
    assert mean([1, 2, 3, 4]) == 2.5


def test_mean_empty():
    with pytest.raises(ValueError):
        mean([])


def test_median_odd_unsorted():
    from stats import median
    assert median([3, 1, 2]) == 2


def test_median_even():
    from stats import median
    assert median([4, 1, 3, 2]) == 2.5
