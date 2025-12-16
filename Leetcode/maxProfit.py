class Solution:
    def maxProfit(self, prices):
        buy_price = prices[0]
        profit = 0

        for i in prices[1:]:
            if buy_price > i:
                buy_price = i
            profit = max(profit, i - buy_price)
        return profit


sol = Solution()
print(sol.maxProfit(prices=[7, 1, 5, 3, 6, 4]))
