class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = int(1e9)
        res = 0
        for price in prices:
            minPrice = min(minPrice, price)
            res = max(res, price - minPrice)
        return res