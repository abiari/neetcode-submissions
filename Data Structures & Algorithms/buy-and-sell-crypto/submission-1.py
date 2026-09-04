class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        n_days = len(prices)
        max_profit = 0
        for day in range(1, n_days):
            day_profit = prices[day] - lowest_price
            if day_profit <= 0:
                lowest_price = prices[day]
                continue
            max_profit = max(max_profit, day_profit)
        return max_profit