def subarray_sum_fixed(nums: list[int], k: int) -> int:
    n = len(nums)
    window_sum = sum(nums[:k])
    largest = window_sum
    for i in range(1, n - k):
        window_sum = window_sum - nums[i - 1] + nums[i + k - 1]
        if window_sum > largest:
            largest = window_sum
    return window_sum


def test_1():
    assert subarray_sum_fixed(nums=[1, 2, 3, 7, 4, 1], k=3) == 14
