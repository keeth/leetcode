class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i = 0
        j = m
        while i < m + n:
            if nums2:
                if i >= j:
                    nums1[i] = nums2.pop(0)
                elif nums2[0] < nums1[i]:
                    nums1[i : i + 1] = [nums2.pop(0), nums1[i]]
                    nums1.pop()
                    j += 1
            i += 1


def test_merge():
    s = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    s.merge(nums1, m, nums2, n)
    assert nums1 == [1, 2, 2, 3, 5, 6]


def test_merge_2():
    s = Solution()
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    s.merge(nums1, m, nums2, n)
    assert nums1 == [1]


def test_merge_3():
    s = Solution()
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    s.merge(nums1, m, nums2, n)
    assert nums1 == [1]
