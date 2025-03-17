def subarray_sum(arr: list[int], target: int) -> list[int]:
    sums, n = {0: 0}, len(arr)
    cur_sum = 0
    for i in range(n):
        cur_sum += arr[i]
        complement = cur_sum - target
        if complement in sums:
            return [sums[complement], i + 1]
        sums[cur_sum] = i + 1
    return []


def test_1():
    assert subarray_sum([1, -20, -3, 30, 5, 4], 7) == [1, 4]
