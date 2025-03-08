import math
from collections import namedtuple


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        state = namedtuple("state", ["low", "high", "profit"])
        state.low = math.inf
        state.high = -math.inf
        state.profit = 0

        def update_profit():
            if not math.isinf(state.high) and not math.isinf(state.low):
                state.profit += state.high - state.low
                state.low = math.inf
                state.high = -math.inf

        for i in range(n):
            if prices[i] < state.high:
                update_profit()
            if prices[i] < state.low:
                state.low = prices[i]
            elif prices[i] > state.high:
                state.high = prices[i]

        update_profit()

        return state.profit


def test_maxProfit1():
    s = Solution()
    assert s.maxProfit([7, 2, 1, 5, 3, 6, 4]) == 7


def test_maxProfit2():
    s = Solution()
    assert s.maxProfit([1, 2, 3, 4, 5]) == 4


def test_maxProfit3():
    s = Solution()
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0
