from math import inf
from typing import List


class Solution:
    def coinChange1(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[0] + [inf] * amount for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = min(dp[i][j - coins[i - 1]] + 1, dp[i - 1][j])
        return dp[n][amount] if dp[n][amount] < inf else -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [0] + [inf] * amount

        for i in range(1, n + 1):
            for j in range(coins[i - 1], amount + 1):
                dp[j] = min(dp[j - coins[i - 1]] + 1, dp[j])
        return dp[amount] if dp[amount] < inf else -1


