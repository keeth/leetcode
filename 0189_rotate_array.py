class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        if k == 0 or n < 2 or k % n == 0:
            return
        out = [0] * n
        for i in range(n):
            out[(i + k) % n] = nums[i]
        for i in range(n):
            nums[i] = out[i]


def test_rotate1():
    s = Solution()
    a = [1, 2, 3, 4, 5, 6, 7]
    s.rotate(a, 3)
    assert a == [5, 6, 7, 1, 2, 3, 4]


def test_rotate2():
    s = Solution()
    a = [-1, -100, 3, 99]
    s.rotate(a, 2)
    assert a == [3, 99, -1, -100]


def test_rotate3():
    s = Solution()
    a = [1, 2, 3, 4, 5, 6]
    s.rotate(a, 3)
    assert a == [4, 5, 6, 1, 2, 3]


def test_rotate4():
    s = Solution()
    a = [1, 2, 3, 4, 5, 6]
    s.rotate(a, 0)
    assert a == [1, 2, 3, 4, 5, 6]


def test_rotate5():
    s = Solution()
    a = [1, 2]
    s.rotate(a, 2)
    assert a == [1, 2]


def test_rotate6():
    s = Solution()
    a = [1, 2, 3, 4, 5, 6]
    s.rotate(a, 4)
    assert a == [3, 4, 5, 6, 1, 2]
