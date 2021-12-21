class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        lowest = prices[0]
        best = 0
        for i in range(len(prices)):
            if prices[i] < lowest:
                lowest = prices[i] # Buy now...
            else:
                best = max(best, prices[i] - lowest) # Or, sell now...
        return best
