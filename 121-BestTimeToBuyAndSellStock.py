from typing import List

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for price in prices:
            min_price = min(min_price,price)
            profit = price - min_price
            max_profit = max(max_profit,profit)
        return max_profit


sol = Solution()
mylist = [7, 1, 5, 3, 6, 4]
print(sol.maxProfit(mylist))