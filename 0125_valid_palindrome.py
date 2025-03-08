import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        s = re.sub(r"[^A-Za-z0-9]", "", s).lower()
        if len(s) == 1:
            return True

        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True


def test_is_palindrome1():
    s = Solution()
    assert s.isPalindrome("A man, a plan, a canal: Panama")


def test_is_palindrome2():
    s = Solution()
    assert not s.isPalindrome("race a car")


def test_is_palindrome3():
    s = Solution()
    assert s.isPalindrome(" ")
