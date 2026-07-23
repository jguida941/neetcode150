import pytest

from arrays_hashing.p01_contains_duplicate import Solution as ContainsDuplicate


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 3], True),
        ([1, 2, 3, 4], False),
        ([], False),
        ([1], False),
        ([1, 1], True),
        ([-(10**9), 10**9, -(10**9)], True),
    ],
)
def test_has_duplicate(nums, expected):
    assert ContainsDuplicate().hasDuplicate(nums) is expected
