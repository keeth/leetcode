class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:

        return False


def test_0():
    s = Solution()
    assert s.wordPatternMatch(pattern="abab", s="redblueredblue")
    assert s.wordPatternMatch(pattern="aaaa", s="asdasdasdasd")
    assert not s.wordPatternMatch(pattern="aabb", s="xyzabcxzyabc")
