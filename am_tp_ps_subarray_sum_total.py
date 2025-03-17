from collections import defaultdict


def subarray_sum_total(arr: list[int], target: int) -> list[int]:
    sums = defaultdict(int)
    sums[0] = 1
    cur_sum = 0
    count = 0
    for val in arr:
        cur_sum += val
        complement = cur_sum - target
        if complement in sums:
            count += sums[complement]
        sums[cur_sum] = 1
    return count


def test_1():
    assert subarray_sum_total([1, 2, 3], 3) == 2
