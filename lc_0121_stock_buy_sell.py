class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0

        low = prices[0]
        max_profit = 0
        for price in prices[1:]:
            if price < low:
                low = price
            else:
                profit = price - low
                if profit > max_profit:
                    max_profit = profit
        return max_profit


def test_maxProfit1():
    s = Solution()
    assert s.maxProfit([7, 2, 1, 5, 3, 6, 4]) == 5


def test_maxProfit2():
    s = Solution()
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0


def test_maxProfit3():
    s = Solution()
    assert s.maxProfit([1, 2]) == 1


def test_maxProfit4():
    s = Solution()
    assert s.maxProfit([3, 2, 6, 5, 0, 3]) == 4
