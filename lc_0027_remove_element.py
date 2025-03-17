class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        j = 0
        n = len(nums)
        while i + j < n:
            if nums[i] == val:
                nums.pop(i)
                j += 1
            else:
                i += 1
        return i


def test_remove_element():
    s = Solution()
    a = [3, 2, 2, 3]
    assert s.removeElement(a, 3) == 2
    assert sorted(a[:2]) == sorted([2, 2])


def test_remove_element_2():
    s = Solution()
    a = [0, 1, 2, 2, 3, 0, 4, 2]
    assert s.removeElement(a, 2) == 5
    assert sorted(a[:5]) == sorted([0, 1, 4, 0, 3])


def test_remove_element_3():
    s = Solution()
    a = [2]
    assert s.removeElement(a, 3) == 1
    assert sorted(a[:1]) == sorted([2])


def test_remove_element_4():
    s = Solution()
    a = [1]
    assert s.removeElement(a, 1) == 0
    assert sorted(a) == sorted([])
