class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount == 1:
            return 1 if 1 in coins else -1
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(len(dp)):
            for c in coins:
                if i - c < 0:
                    continue
                dp[i] = min(dp[i], dp[i - c] + 1)
        
        return dp[-1] if dp[-1] != float('inf') else -1     
        
        
        
