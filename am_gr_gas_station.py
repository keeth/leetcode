from typing import List


def starting_station(gas: List[int], dist: List[int]) -> int:
    return 0


def test_0():
    gas = [1, 2, 3, 4, 5]
    dist = [3, 4, 5, 1, 2]
    assert starting_station(gas, dist) == 3
