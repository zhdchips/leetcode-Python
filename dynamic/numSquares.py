class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        square = [num * num for num in range(1, (int)(n**0.5 + 1))]
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = i
            for s in square:
                if s > i:
                    break
                dp[i] = min(dp[i], dp[i - s] + 1)

        return dp[n]