class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n_days = len(prices)
        i = 0
        max_profit = 0
        while i < n_days:
            j = i + 1
            while j < n_days:
                max_profit = max(max_profit, prices[j] - prices[i])
                j += 1
            i += 1 
        return max_profit